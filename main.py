import numpy as np
import pygame as pg
from dir import right,left,up,down,no
from node import NodeWeb



pg.init()
screen=pg.display.set_mode((800,600))
clock=pg.Clock()
circle=pg.surface.Surface((10,10))
counter=0
pg.draw.circle(circle,"white",(5,5),5)


sprites=pg.sprite.Group()
arr: dict[tuple[int, int], object] = {(x, y): 0 for x in range(80) for y in range(60)}
class Dot(pg.sprite.Sprite):
	def __init__(self,pos, *groups) -> None:
		super().__init__(*groups)
		sprites.add(self)
		self.image:pg.Surface=circle.copy()
		self.rect=self.image.get_rect()
		self.pos:list[int]=list((int(pos[0]),(int(pos[1]))))
		arr[pos]=self
		self.web=NodeWeb(7,5)
		self.web.populate(10)
		self.counter=0

	def move(self,dir):
		buff=self.pos
		if self.pos_check(dir):  # type: ignore
			if dir == no:
				return 0
			if dir == right:
				self.pos[0] += 1
			if dir == left:
				self.pos[0] -= 1
			if dir == up:
				self.pos[1] -= 1
			arr[tuple(buff)] = 0  # type: ignore
			arr[tuple(self.pos)] = self  # type: ignore
			return 1
		else:
			return 0
	
	def pos_check(self,dir):
		buff = self.pos.copy()
		if dir==no:
			return 0
		if dir==right:
			buff[0]+=1
		if dir==left:
			buff[0]-=1
		if dir==up:
			buff[1]-=1
		if dir==down:
			buff[1]+=1
		if -1 < buff[0] < 80 and -1 < buff[1] < 60 and not arr[tuple(buff)]: # type: ignore
			return 1
		return 0

	def action(self):
		inputs = [self.pos[0]/80 , self.pos[1]/60 ,(self.pos_check(right)),(self.pos_check(up)),bool(self.pos_check(left)),bool(self.pos_check(down)),self.counter%5/4 ]
		self.web.set_inputs(inputs)
		self.web.forward()
		outputs=self.web.get_outputs()
		ix=outputs.index(max(outputs))
		dir=[right,up,left,down,no][ix]
		self.move(dir)


	def update(self):
		self.action()
		mutation_interval=15
		if self.counter%mutation_interval==0:
			lr=1
			dist2=(self.pos[0]-40)**2+(self.pos[1]-30)**2
			if dist2<400:
				lr=0.1
				if dist2<225:
					lr=0.01
			self.web.mutate(lr)

		self.rect.topleft = tuple(np.array(self.pos) * 10) # type: ignore
		self.counter+=1


pos = np.random.choice(4800, size=400,replace=False)
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
	if counter%30==0:
		print(clock.get_fps())
	
	clock.tick()
	counter+=1
	