from node import NodeWeb
import random

ixes=[]
N=6
Ppl=6
for i in range(100):
	web=NodeWeb(N,N)
	web.populate(Ppl)
	l=[]
	for i in range(100):
		ins=[]
		for i in range(N):
			ins.append(random.random())
		web.set_inputs(ins)
		web.forward()
		
		out=web.get_outputs()
		web.mutate(1)
		ix=out.index(max(out))
		l.append(ix)
	ix1=l.count(0)
	ixes.append(ix1)
print(sum(ixes)/100)
