import numpy as np
import pygame as pg
import random
from neat_core import Genome, NeuralNetwork, NodeType, global_innovation_tracker

class Agent(pg.sprite.Sprite):
    def __init__(self, pos, genome=None, world=None):
        super().__init__()
        self.world = world
        self.pos = list(pos)
        self.energy = 50.0
        self.age = 0

        if genome is None:
            # Inputs: x, y, food, temp, energy, clock1, clock2, age
            # Outputs: Right, Left, Up, Down, Eat, Reproduce
            self.genome = Genome(8, 6)
            # Initial random connections
            for _ in range(10):
                self.genome.mutate_add_connection(global_innovation_tracker)
        else:
            self.genome = genome

        self.nn = NeuralNetwork(self.genome)
        self.size = self.genome.traits.get("size", 1.0)
        self.metabolism = self.genome.traits.get("metabolism", 1.0)

        # Sprite setup
        self.image = pg.Surface((int(5 * self.size + 2), int(5 * self.size + 2)), pg.SRCALPHA)
        color = self.get_color()
        pg.draw.circle(self.image, color, (self.image.get_width()//2, self.image.get_height()//2), int(2.5 * self.size))
        self.rect = self.image.get_rect()
        self._update_rect()

        self.dead = False
        self.wants_reproduce = False

    def get_color(self):
        # Color based on metabolism (Red for high, Blue for low)
        r = int(np.clip(self.metabolism * 127, 0, 255))
        b = int(np.clip((2.0 - self.metabolism) * 127, 0, 255))
        return (r, 100, b)

    def _update_rect(self):
        self.rect.center = (self.pos[0] * 10 + 5, self.pos[1] * 10 + 5)

    def update(self):
        if self.dead: return

        self.age += 1
        # Energy consumption
        # Base cost + size cost + metabolism cost
        cost = 0.1 + (self.size * 0.1) + (self.metabolism * 0.2)
        self.energy -= cost

        if self.energy <= 0 or self.age > 1000:
            self.dead = True
            return

        # Temperature effects
        temp = self.world.get_temp(self.pos[0], self.pos[1])
        # Ideal temp is 15. Deviations cost energy.
        temp_cost = abs(temp - 15) * 0.01 * self.size
        self.energy -= temp_cost

        # Brain inputs
        local_info = self.world.get_local_info(self.pos[0], self.pos[1])
        inputs = [
            self.pos[0] / self.world.width,
            self.pos[1] / self.world.height,
            local_info["food_density"] / 10.0,
            (local_info["temp"] + 10) / 40.0,
            self.energy / 100.0,
            np.sin(self.age * 0.1),
            np.cos(self.age * 0.1),
            self.age / 1000.0
        ]

        outputs = self.nn.activate(inputs)

        # Decide action
        action_idx = np.argmax(outputs)

        if action_idx == 0: # Right
            self.move(1, 0)
        elif action_idx == 1: # Left
            self.move(-1, 0)
        elif action_idx == 2: # Up
            self.move(0, -1)
        elif action_idx == 3: # Down
            self.move(0, 1)
        elif action_idx == 4: # Eat
            self.eat()
        elif action_idx == 5: # Reproduce
            if self.energy > 80:
                self.wants_reproduce = True

    def move(self, dx, dy):
        self.pos[0] = (self.pos[0] + dx) % self.world.width
        self.pos[1] = (self.pos[1] + dy) % self.world.height
        self.energy -= 0.05 * self.size # Movement cost
        self._update_rect()

    def eat(self):
        amount = self.world.consume_food(self.pos[0], self.pos[1])
        self.energy += amount * 10.0 # Nutrition
        self.energy = min(self.energy, 200.0)
