import numpy as np
from numpy.typing import NDArray
import pygame as pg

from agent import sprites,arr,Agent


DOT_COUNT = 4000

pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.Clock()
circle = pg.surface.Surface((10, 10))
counter = 0
pg.draw.circle(circle, "white", (5, 5), 5)



class Dot(Agent):
    def __init__(self, pos, *groups) -> None:
        super().__init__(pos, *groups)
    def reward(self):
        mutation_interval = 10
        if self.counter % mutation_interval == 0:
            lr = 0.2
            if self.is_at_edge:
                lr = 1
            dist2 = abs(self.pos[0] - 40) + abs(self.pos[1] - 30)
            if dist2 < 15:
                lr = 0.01
            self.web.mutate(lr)
        if self.is_moved:
            self._update_rect()

pos = np.random.choice(4800, size=DOT_COUNT, replace=False)
for i in pos:
    p = (i % 80, i // 80)
    Dot(p)



while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    sprites.update()
    screen.fill("black")
    sprites.draw(screen)
    pg.display.flip()
    if counter % 300 == 0:
        print(int(clock.get_fps()))

    clock.tick()
    counter += 1
