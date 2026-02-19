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
    pg.font.init()
    font = pg.font.Font(None, 24)

    width = config["world"]["width"]
    height = config["world"]["height"]
    tile_size = config["world"]["tile_size"]
    fps = config["simulation"]["fps"]

    screen = pg.display.set_mode((width * tile_size, height * tile_size))
    pg.display.set_caption("Evolution Sim")
    clock = pg.Clock()

    world = World(config)
    agents = pg.sprite.Group()

    avg_energy = 0
    avg_age = 0
    last_stats_update = 0

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

        # Build spatial grid for optimized mate searching
        grid = [[set() for _ in range(height)] for _ in range(width)]
        for a in agents:
            grid[a.pos[0]][a.pos[1]].add(a)

        new_agents = []
        already_mated = set()
        for agent in list(agents):
            if agent in already_mated: continue

            old_pos = (agent.pos[0], agent.pos[1])
            agent.update()
            new_pos = (agent.pos[0], agent.pos[1])

            # Update grid as agent moves
            if old_pos != new_pos:
                grid[old_pos[0]][old_pos[1]].discard(agent)
                grid[new_pos[0]][new_pos[1]].add(agent)

            if agent.dead:
                agent.kill()
                grid[new_pos[0]][new_pos[1]].discard(agent)
            elif agent.wants_reproduce:
                # Try Sexual reproduction first (Optimized with Spatial Grid)
                mate = None
                found_mate = False
                # Check 13 tiles within Manhattan distance 2 (non-wrapping to match original)
                for dx in range(-2, 3):
                    for dy in range(-(2 - abs(dx)), 2 - abs(dx) + 1):
                        nx, ny = new_pos[0] + dx, new_pos[1] + dy
                        if 0 <= nx < width and 0 <= ny < height:
                            for other in grid[nx][ny]:
                                if (other != agent and other not in already_mated and
                                    not other.dead and other.wants_reproduce):
                                    # dist is guaranteed <= 2 by tile selection
                                    if agent.genome.compatibility_distance(other.genome) < 3.0:
                                        mate = other
                                        found_mate = True
                                        break
                            if found_mate: break

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

        # Draw temperature/food background using optimized numpy/surfarray approach
        food_colors = np.zeros((width, height, 3), dtype=np.uint8)
        food_greens = np.clip(world.food * 25, 0, 255).astype(np.uint8)
        food_mask = world.food > 0.1
        food_colors[food_mask, 1] = food_greens[food_mask]

        # Upscale food to tiles
        background_pixels = np.repeat(np.repeat(food_colors, tile_size, axis=0), tile_size, axis=1)

        # Draw temperature lines
        temp_color_vals = np.clip((world.temperature + 10) / 40 * 255, 0, 255).astype(np.uint8)
        row_indices = np.arange(height) * tile_size + (tile_size - 1)
        temp_repeats = np.repeat(temp_color_vals, tile_size, axis=0)

        background_pixels[:, row_indices, 0] = temp_repeats
        background_pixels[:, row_indices, 2] = 255 - temp_repeats
        background_pixels[:, row_indices, 1] = 0 # Ensure no green from food on the temp line

        pg.surfarray.blit_array(screen, background_pixels)

        agents.draw(screen)

        # HUD
        current_time = pg.time.get_ticks()
        if current_time - last_stats_update > 500:  # Update stats every 500ms
            if len(agents) > 0:
                avg_energy = sum(a.energy for a in agents) / len(agents)
                avg_age = sum(a.age for a in agents) / len(agents)
            last_stats_update = current_time

        # Render stats
        stats = [
            f"FPS: {clock.get_fps():.1f}",
            f"Agents: {len(agents)}",
            f"Avg Energy: {avg_energy:.1f}",
            f"Avg Age: {avg_age:.1f}"
        ]

        # Draw semi-transparent background
        bg_surface = pg.Surface((200, 100), pg.SRCALPHA)
        bg_surface.fill((0, 0, 0, 128))
        screen.blit(bg_surface, (10, 10))

        for i, line in enumerate(stats):
            text_surface = font.render(line, True, (255, 255, 255))
            screen.blit(text_surface, (20, 20 + i * 20))

        pg.display.flip()
        clock.tick(fps)

        if len(agents) == 0:
            print("Extinction!")
            running = False

    pg.quit()

if __name__ == "__main__":
    main()
