from node import NodeWeb, Node, OutputNode
import random


class WebTest(NodeWeb):

    def print(self):
        for node in self.inputs:
            cursor:Node = node
            print("i->", end="")
            while cursor.next:
                cursor = cursor.next
                if not isinstance(cursor,OutputNode):
                    print("m->", end="")
                else:
                    print("o", end="")
            print() 
ixes=[]
N=6
Ppl=6

web=WebTest(N,N)
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
ix1=l.count(5)
print(ix1)
web.print()


