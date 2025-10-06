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

def web_test(test_print=False,web_forward=True):
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


        max_val = max(out)
        max_indices = [i for i, x in enumerate(out) if x == max_val]
        ix = random.choice(max_indices)


        l.append(ix)
    out=l.count(0)
    if test_print:
        print(out)
        web.print()
    return out

total0=0
for i in range(1000):
    total0+=web_test()
print(total0/100000)
