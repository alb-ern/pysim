class Dir:
	def set_opposite(self,dir: "Dir"):
		self.opposite=dir
		dir.opposite=self
	pass

right=Dir()
left=Dir()
up=Dir()
down=Dir()
right.set_opposite(left)
up.set_opposite(down)

