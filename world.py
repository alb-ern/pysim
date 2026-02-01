import numpy as np
import random

class World:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.food = np.zeros((width, height), dtype=np.float32)
        self.temperature = np.zeros((width, height), dtype=np.float32)

        # Initialize temperature gradient (Top is cold, Bottom is hot)
        for y in range(height):
            self.temperature[:, y] = (y / height) * 40 - 10  # Range: -10 to 30

        # Initial food
        self.food = np.random.uniform(0, 2, (width, height)).astype(np.float32)

    def update(self):
        # Regrow food: 1% chance per tile to grow some food
        regrow_mask = np.random.random((self.width, self.height)) < 0.01
        self.food[regrow_mask] += 1.0
        # Slowly regrow everywhere
        self.food += 0.001
        self.food = np.clip(self.food, 0, 10)

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
