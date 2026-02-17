import pygame as pg
import random
import numpy as np
import json
import os
from world import World
from agent import Agent
from neat_core import global_innovation_tracker, Genome

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def main():
    config = load_config()

    pg.init()
    width = config["world"]["width"]
    height = config["world"]["height"]
    tile_size = config["world"]["tile_size"]
    fps = config["simulation"]["fps"]

    screen = pg.display.set_mode((width * tile_size, height * tile_size))
    pg.display.set_caption("Evolution Sim")
    clock = pg.Clock()
    font = pg.font.SysFont(None, 24)

    world = World(config)
    agents = pg.sprite.Group()

    # Initial population
    for _ in range(config["agent"]["initial_population"]):
        pos = (random.randint(0, width - 1), random.randint(0, height - 1))
        agents.add(Agent(pos, config, world=world))

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Update
        world.update()

        new_agents = []
        already_mated = set()
        for agent in list(agents):
            if agent in already_mated: continue
            agent.update()
            if agent.dead:
                agent.kill()
            elif agent.wants_reproduce:
                # Try Sexual reproduction first
                mate = None
                for other in agents:
                    if (other != agent and other not in already_mated and
                        not other.dead and other.wants_reproduce):
                        dist = abs(agent.pos[0] - other.pos[0]) + abs(agent.pos[1] - other.pos[1])
                        if dist <= 2: # Within reach
                            if agent.genome.compatibility_distance(other.genome) < 3.0:
                                mate = other
                                break

                if mate:
                    agent.wants_reproduce = False
                    mate.wants_reproduce = False
                    agent.energy -= config["agent"]["sexual_reproduce_cost"]
                    mate.energy -= config["agent"]["sexual_reproduce_cost"]
                    already_mated.add(agent)
                    already_mated.add(mate)

                    child_genome = Genome.crossover(agent.genome, mate.genome)
                    child_genome.mutate_weights(power=0.5)
                    if random.random() < config["neat"]["mutate_add_conn_chance"]:
                        child_genome.mutate_add_connection(global_innovation_tracker)

                    child = Agent(agent.pos, config, genome=child_genome, world=world)
                    new_agents.append(child)
                elif agent.energy > config["agent"]["reproduce_energy_threshold_asexual"]:
                    # Asexual reproduction
                    agent.wants_reproduce = False
                    agent.energy -= config["agent"]["asexual_reproduce_cost"]

                    child_genome = agent.genome.copy()
                    child_genome.mutate_weights(power=0.5)
                    if random.random() < config["neat"]["mutate_add_conn_chance"]:
                        child_genome.mutate_add_connection(global_innovation_tracker)
                    if random.random() < config["neat"]["mutate_add_node_chance"]:
                        child_genome.mutate_add_node(global_innovation_tracker)

                    child = Agent(agent.pos, config, genome=child_genome, world=world)
                    new_agents.append(child)

        for a in new_agents:
            agents.add(a)

        # Draw
        screen.fill((0, 0, 0))

        # Draw temperature/food background (optional, let's just do food for now)
        # For performance, maybe don't draw every tile every frame
        # But for 80x60 it's fine.
        for x in range(width):
            for y in range(height):
                food_val = world.food[x, y]
                if food_val > 0.1:
                    green = min(255, int(food_val * 25))
                    pg.draw.rect(screen, (0, green, 0), (x * tile_size, y * tile_size, tile_size, tile_size))

                # Temperature indicator (small line at bottom of tile)
                temp = world.temperature[x, y]
                # -10 to 30 -> Blue to Red
                color_val = int(np.clip((temp + 10) / 40 * 255, 0, 255))
                pg.draw.line(screen, (color_val, 0, 255 - color_val),
                             (x * tile_size, (y + 1) * tile_size - 1),
                             ((x + 1) * tile_size, (y + 1) * tile_size - 1))

        agents.draw(screen)

        # Draw HUD
        hud_bg = pg.Surface((220, 100), pg.SRCALPHA)
        hud_bg.fill((0, 0, 0, 150))
        screen.blit(hud_bg, (10, 10))

        agent_count = len(agents)
        avg_energy = 0.0
        avg_age = 0.0
        if agent_count > 0:
            avg_energy = sum(a.energy for a in agents) / agent_count
            avg_age = sum(a.age for a in agents) / agent_count

        stats = [
            f"Agents: {agent_count}",
            f"Avg Energy: {avg_energy:.1f}",
            f"Avg Age: {avg_age:.1f}",
            f"FPS: {clock.get_fps():.1f}"
        ]

        for i, line in enumerate(stats):
            text_surf = font.render(line, True, (255, 255, 255))
            screen.blit(text_surf, (20, 20 + i * 20))

        pg.display.flip()
        clock.tick(fps)

        if pg.time.get_ticks() % 5000 < 33: # Every ~5 seconds
            if len(agents) > 0:
                avg_energy = sum(a.energy for a in agents) / len(agents)
                avg_age = sum(a.age for a in agents) / len(agents)
                print(f"Stats - Agents: {len(agents)}, Avg Energy: {avg_energy:.1f}, Avg Age: {avg_age:.1f}")

        if len(agents) == 0:
            print("Extinction!")
            running = False

    pg.quit()

if __name__ == "__main__":
    main()
