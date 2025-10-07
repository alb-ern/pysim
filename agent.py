import numpy as np
from numpy.typing import NDArray
import pygame as pg

from dir import right, left, up, down, no
from node import NodeWeb





circle = pg.surface.Surface((10, 10))
pg.draw.circle(circle, "white", (5, 5), 5)

sprites = pg.sprite.Group()
arr: NDArray[np.object_] = np.zeros((80, 60), object)


class Agent(pg.sprite.Sprite):
    def __init__(self, pos, *groups) -> None:
        super().__init__(*groups)
        sprites.add(self)
        self.image: pg.Surface = circle.copy()
        self.rect = self.image.get_rect()
        self.pos: list[int] = list((int(pos[0]), (int(pos[1]))))
        arr[pos] = self
        self._update_rect()
        self.web = NodeWeb(8, 5)
        self.web.populate(3)
        self.counter = 0

    def move(self, dir):
        self.is_moved = False
        if dir == no:
            return
        pos = self.pos_check(dir)
        if pos:
            arr[tuple(self.pos)] = 0  # type: ignore
            arr[tuple(pos)] = self  # type: ignore
            self.pos = pos
            self.is_moved = True

    def pos_check(self, dir):
        buff = self.pos.copy()
        if dir == right:
            buff[0] += 1
        if dir == left:
            buff[0] -= 1
        if dir == up:
            buff[1] -= 1
        if dir == down:
            buff[1] += 1
        if -1 < buff[0] < 80 and -1 < buff[1] < 60 and not arr[tuple(buff)]:  # type: ignore
            return buff
        return 0

    def is_at_edge(self):
        if self.pos[0] == 0 or self.pos[0] == 79 or self.pos[1] == 0 or self.pos[1] == 59:
            return True
        return False

    def action(self):
        inputs = [self.pos[0] / 80, self.pos[1] / 60, bool(self.pos_check(right)), bool(self.pos_check(up)), bool(self.pos_check(left)), bool(self.pos_check(down)), self.counter % 5 / 4, self.counter % 15 / 14]
        self.web.set_inputs(inputs)
        self.web.forward()
        ix = self.web.get_max_index()
        dir = [right, up, left, down, no][ix]
        self.move(dir)

    def reward(self):
        pass

    def update(self):
        self.action()
        self.reward()
        self.counter += 1

    def _update_rect(self):
        self.rect.topleft = tuple(np.array(self.pos) * 10)
