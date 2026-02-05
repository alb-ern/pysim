import numpy as np
import random
import json

class World:
    def __init__(self, config):
        self.config = config["world"]
        self.width = self.config["width"]
        self.height = self.config["height"]
        self.food = np.zeros((self.width, self.height), dtype=np.float32)
        self.temperature = np.zeros((self.width, self.height), dtype=np.float32)

        # Initialize temperature gradient (Top is cold, Bottom is hot)
        for y in range(self.height):
            self.temperature[:, y] = (y / self.height) * 40 - 10  # Range: -10 to 30

        # Initial food
        self.food = np.random.uniform(0, self.config["initial_food_density"], (self.width, self.height)).astype(np.float32)

    def update(self):
        # Regrow food: chance per tile to grow some food
        regrow_mask = np.random.random((self.width, self.height)) < self.config["food_regrow_chance"]
        self.food[regrow_mask] += self.config["food_regrow_amount"]
        # Slowly regrow everywhere
        self.food += self.config["food_slow_regrow"]
        self.food = np.clip(self.food, 0, self.config["food_max_cap"])

    def consume_food(self, x, y):
        ix, iy = int(x) % self.width, int(y) % self.height
        amount = self.food[ix, iy]
        self.food[ix, iy] = 0
        return amount

    def get_temp(self, x, y):
        ix, iy = int(x) % self.width, int(y) % self.height
        return self.temperature[ix, iy]

    def get_local_info(self, x, y):
        ix, iy = int(x) % self.width, int(y) % self.height
        # Surroundings (3x3 area)
        food_sum = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                food_sum += self.food[(ix + dx) % self.width, (iy + dy) % self.height]

        return {
            "food_density": food_sum / 9.0,
            "temp": self.temperature[ix, iy]
        }
