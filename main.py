import numpy as np
import pygame as pg
from dir import right,left,up,down



pg.init()
screen=pg.display.set_mode((800,600))
clock=pg.Clock()
circle=pg.surface.Surface((10,10))
pg.draw.circle(circle,"white",(5,5),5)


sprites=pg.sprite.Group()
arr: dict[tuple[int, int], object] = {(x, y): 0 for x in range(80) for y in range(60)}
class Dot(pg.sprite.Sprite):
	def __init__(self,pos, *groups) -> None:
		super().__init__(*groups)
		sprites.add(self)
		self.image=circle
		self.rect=self.image.get_rect()
		self.pos:list[int]=list((int(pos[0]),(int(pos[1]))))
		arr[pos]=self

	def move(self,dir):
		buff=self.pos.copy()
		if dir==right:
			self.pos[0]+=1
		if dir==left:
			self.pos[0]-=1
		if dir==up:
			self.pos[1]-=1
		if dir==down:
			self.pos[1]+=1

		if -1<self.pos[0]<80 and -1<self.pos[1]<60 and not arr[tuple(self.pos)]: # type: ignore
			arr[tuple(self.pos)] = self  # type: ignore
			arr[tuple(buff)] = 0  # type: ignore
		else:
			self.pos=buff



	def update(self):
		dir=np.random.choice(np.array([right,left,up,down]))
		self.move(dir)
		self.rect.topleft = tuple(np.array(self.pos) * 10)


pos = np.random.choice(4800, size=500,replace=False)
for i in pos:
	p=(i%80,i//80)
	Dot(p)


while True:
	for event in pg.event.get():
		if event.type==pg.QUIT:
			pg.quit()
			exit()
	sprites.update()
	screen.fill("black")
	sprites.draw(screen)
	pg.display.flip()
	clock.tick(30)