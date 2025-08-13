import math
import random
import matplotlib.pyplot as plt
import numpy as np


def clamp(x:float):
    return min(max(x,-1),1)
# Activation functions
def sigmoid(x: float) -> float:
    """Standard sigmoid activation function"""
    try:
        return 2.0 / (1.0 + math.exp(-4*x))-1
    except OverflowError:
        return 0.0 if x < 0 else 1.0



def cube(x:float):
    return x**3


def tanh_activation(x: float) -> float:
    """Hyperbolic tangent activation function"""
    return math.tanh(x)


def relu(x: float) -> float:
    """ReLU activation function"""
    return max(0.0, x)


def leaky_relu(x: float, alpha: float = 0.01) -> float:
    """Leaky ReLU activation function"""
    return x if x > 0 else alpha * x
def sin(x:float):
    return math.sin(4*x)


def inv(x:float):
    return sigmoid(1/(10*x)) if x!=0 else 0

def sign(x:float):
    return -x

funcs = [clamp,sigmoid, leaky_relu, cube, abs,sign]


class Node:
    def __init__(self,prev=None) -> None:
        self.next: Node | None = None
        self.prev: Node | None = prev
        self.data: float
        self.web:"NodeWeb|None"
        if prev:
            prev.next=self
    def connect_to(self,to):
        self.next=to
        to.prev=self
    def connect_from(self,from_):
        self.prev=from_
        from_.next=self
    def add_to(self,web):
        self.web=web
    

class MidNode(Node):
    def __init__(self, prev,next) -> None:
        super().__init__(prev)
        self.next=next
        next.prev=self
        self.f = random.choice(funcs)
        self.w = random.uniform(0.8, 1.25)
        self.b = random.uniform(-0.1, 0.1)
    def func(self):
        self.data = clamp(self.f(self.prev.data))
    def remove(self):
        if isinstance(self.prev, InputNode) and isinstance(self.next, OutputNode):
            self.prev.next=None
            self.next.prev=None
        elif self.prev and self.next:
            self.prev.connect_to(self.next)
            self.web.mids.remove(self)
        
class InputNode(Node):
    def __init__(self):
        super().__init__(None)
    def set_data(self,data:float):
        self.data=data


class OutputNode(Node):
    def __init__(self, prev=None) -> None:
        super().__init__(prev)
    def func(self):
        self.data=self.prev.data

class NodeWeb:
    def __init__(self,in_size:int,out_size:int) -> None:
        self.inputs=[]
        self.free_inputs=[]
        self.outputs=[]
        self.free_outputs=[]
        self.mids=[]
        for i in range(in_size):
            in_node=InputNode()
            self.add(in_node)
        for i in range(out_size):
            out_node=OutputNode()
            self.add(out_node)
    def add(self,node: Node):
        node.add_to(self)
        if isinstance(node,InputNode):
            self.inputs.append(node)
            self.free_inputs.append(node)
        if isinstance(node,OutputNode):
            self.outputs.append(node)
            self.free_outputs.append(node)
        if isinstance(node,MidNode):
            self.mids.append(node)
    def insert(self,node):
        if node.next:
            new=MidNode(node,node.next)
            self.add(new)
        else:#bridge case
            if len(self.free_outputs)>0:
                free=random.choice(self.free_outputs)
                new=MidNode(node,free)
                self.add(new)
                self.free_inputs.remove(node)
                self.free_outputs.remove(free)
    def populate(self,n:int=10):
        assert n <len(self.outputs)#TODO: make better fix
        for i in range(n):
            from_=random.choice(self.inputs)
            self.insert(from_)
    def forward(self):
        functional_inputs=[x for x in self.inputs if x not in self.free_inputs]
        for node in functional_inputs:
            cursor=node
            while cursor.next:
                cursor=cursor.next
                cursor.func()
    def mutate(self,lr):
        p=random.random()
        l=len(self.mids)
        if 0<l<10:
            self.mutator(p,0.2,0.9)
        elif l<15:
            self.mutator(p, 0.5, 0.95)
        else:
            self.mutator(p,0.7,0.95)
    def mutator(self,p,x,y):
        if p < x:
            to_remove = random.choice(self.mids)
            to_remove.remove()
        elif p<y:
            to_add=random.choice(self.mids)
            self.insert(to_add)
        else:
            to_add = random.choice(self.mids)
            self.insert(to_add)

def main():
    # Create x values
    x = np.linspace(-1, 1, 100)  # 1000 points from -5 to 5

    # Calculate y values for each activation function
    y_sigmoid = [sigmoid(val) for val in x]
    y_tanh = [tanh_activation(val) for val in x]
    y_relu = [relu(val) for val in x]
    y_leaky_relu = [leaky_relu(val) for val in x]
    y_sin=[sin(val) for val in x]
    y_inv = [inv(val) for val in x]

    # Create the plot
    plt.figure(figsize=(9,6),facecolor="gray")

    # Plot each function
    plt.subplot(2, 3, 1)
    plt.plot(x, y_sigmoid, 'b-', linewidth=2, label='Sigmoid')
    plt.title('Sigmoid Function')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.ylim(-1, 1)
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 3, 2)
    plt.plot(x, y_tanh, 'r-', linewidth=2, label='Tanh')
    plt.title('Tanh Function')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.ylim(-1, 1)
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 3, 3)
    plt.plot(x, y_relu, 'g-', linewidth=2, label='ReLU')
    plt.title('ReLU Function')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.ylim(-1, 1)
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 3, 4)
    plt.plot(x, y_leaky_relu, 'm-', linewidth=2, label='Leaky ReLU')
    plt.title('Leaky ReLU Function')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.ylim(-1, 1)
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 3, 5)
    plt.plot(x, y_sin, 'm-', linewidth=2, label='Sin')
    plt.title('Sin')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.ylim(-1, 1)
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 3, 6)
    plt.plot(x, y_inv, 'm-', linewidth=2, label='Inv')
    plt.title('Inv')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.ylim(-1, 1)
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()


if __name__=="__main__":
    main()