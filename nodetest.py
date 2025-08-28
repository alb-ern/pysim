from node import NodeWeb
import random


web=NodeWeb(2,2)
web.populate(2)
l=[]
for i in range(100):
	a=random.random()
	b=random.random()
	web.set_inputs([a,b])
	web.forward()
	web.mutate(1)
	out=web.get_outputs()
	ix=out.index(max(out))
	l.append(ix)
ix1=l.count(0)
print(ix1)

