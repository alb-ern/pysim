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
        self.rng = np.random.default_rng()
        self.food = self.rng.uniform(0, self.config["initial_food_density"], (self.width, self.height)).astype(np.float32)

        # Pre-allocate buffers for performance
        self._regrow_mask = np.empty((self.width, self.height), dtype=bool)

    def update(self):
        # Regrow food: chance per tile to grow some food
        # Using a Generator with float32 reduces memory allocation and is generally faster
        np.less(self.rng.random((self.width, self.height), dtype=np.float32),
                self.config["food_regrow_chance"], out=self._regrow_mask)
        np.add(self.food, self.config["food_regrow_amount"], where=self._regrow_mask, out=self.food)

        # Slowly regrow everywhere
        self.food += self.config["food_slow_regrow"]

        # Clip in-place to avoid allocating a new full-grid array
        np.clip(self.food, 0, self.config["food_max_cap"], out=self.food)

    def consume_food(self, x, y):
        ix, iy = int(x) % self.width, int(y) % self.height
        amount = self.food[ix, iy]
        self.food[ix, iy] = 0
        return amount

    def get_temp(self, x, y):
        ix, iy = int(x) % self.width, int(y) % self.height
        return self.temperature[ix, iy]

    def get_local_info(self, x, y):
        # Pre-calculate wrapped indices for 3x3 area
        ix, iy = int(x), int(y)
        ix0 = ix % self.width
        ixm1 = (ix - 1) % self.width
        ixp1 = (ix + 1) % self.width
        iy0 = iy % self.height
        iym1 = (iy - 1) % self.height
        iyp1 = (iy + 1) % self.height

        # Unrolled sum for performance
        food_sum = (
            self.food[ixm1, iym1] + self.food[ixm1, iy0] + self.food[ixm1, iyp1] +
            self.food[ix0,  iym1] + self.food[ix0,  iy0] + self.food[ix0,  iyp1] +
            self.food[ixp1, iym1] + self.food[ixp1, iy0] + self.food[ixp1, iyp1]
        )

        return {
            "food_density": food_sum / 9.0,
            "temp": self.temperature[ix0, iy0]
        }
