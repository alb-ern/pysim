from world import World
from agent import Agent
from neat_core import global_innovation_tracker
import pygame as pg

def test_sim_step():
    pg.init()
    pg.display.set_mode((1, 1), pg.NOFRAME) # Small headless-ish window
    width, height = 80, 60
    world = World(width, height)
    agent = Agent((40, 30), world=world)

    print(f"Initial energy: {agent.energy}")
    agent.update()
    print(f"Energy after one update: {agent.energy}")

    # Check if we can eat
    world.food[40, 30] = 5.0
    agent.eat()
    print(f"Energy after eating: {agent.energy}")

    pg.quit()

if __name__ == "__main__":
    test_sim_step()
    print("Integration test passed!")
