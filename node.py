import random
from funcs import funcs,clamp




class Node:
    def __init__(self, prev=None) -> None:
        self.next: Node | None = None
        self.prev: Node | None = prev
        self.data: float
        self.web: "NodeWeb|None"
        if prev:
            prev.next = self

    def connect_to(self, to):
        self.next = to
        to.prev = self

    def connect_from(self, from_):
        self.prev = from_
        from_.next = self

    def add_to(self, web):
        self.web = web
    def func(self):
        pass



class MidNode(Node):
    def __init__(self, prev, next) -> None:
        super().__init__(prev)
        self.next = next
        next.prev = self
        self.f = random.choice(funcs)
        self.w = random.uniform(0.8, 1.25)
        self.b = random.uniform(-0.1, 0.1)

    def func(self):
        self.data = clamp(self.f(self.prev.data*self.w+self.b))


    def remove(self):
        if isinstance(self.prev, InputNode) and isinstance(self.next, OutputNode):
            self.prev.next = None
            self.next.prev = None
        elif self.prev and self.next:
            self.prev.connect_to(self.next)
            self.web.mids.remove(self)


class InputNode(Node):
    def __init__(self):
        super().__init__(None)

    def set_data(self, data: float):
        self.data = data


class OutputNode(Node):
    def __init__(self, prev=None) -> None:
        super().__init__(prev)

    def func(self):
        self.data = self.prev.data
    def get_data(self):
        if not self.prev:
            self.data=0
        return self.data


class NodeWeb:
    def __init__(self, in_size: int, out_size: int) -> None:
        self.inputs:list[InputNode] = []
        self.free_inputs: list[InputNode] = []
        self.outputs: list[OutputNode] = []
        self.free_outputs: list[OutputNode] = []
        self.mids: list[MidNode] = []
        for i in range(in_size):
            in_node = InputNode()
            self._add(in_node)
        for i in range(out_size):
            out_node = OutputNode()
            self._add(out_node)

    def _add(self, node: Node):
        node.add_to(self)
        if isinstance(node, InputNode):
            self.inputs.append(node)
            self.free_inputs.append(node)
        if isinstance(node, OutputNode):
            self.outputs.append(node)
            self.free_outputs.append(node)
        if isinstance(node, MidNode):
            self.mids.append(node)

    def _insert(self, node):
        if node.next:
            new = MidNode(node, node.next)
            self._add(new)
        else:  # bridge case
            if len(self.free_outputs) > 0:
                free = random.choice(self.free_outputs)
                new = MidNode(node, free)
                self._add(new)
                self.free_inputs.remove(node)
                self.free_outputs.remove(free)

    def populate(self, n: int = 10):
        """makes bridges from inputs to outputs for initialization

        Args:
            n (int): count of bridges to be built. Defaults to 10.
        """
        #assert n < len(self.outputs)  # TODO: make better fix
        for i in range(n):
            from_ = random.choice(self.free_inputs)
            self._insert(from_)
    
    def set_inputs(self,inputs:list[float])->None:
        for i in range(len(self.inputs)):
            data = inputs[i]*2-1
            self.inputs[i].set_data(data)

    def get_outputs(self)->list[float]:
        outputs=[]
        for i in range(len(self.outputs)):
            data = self.outputs[i].get_data()
            outputs.append(data)
        return outputs

    def forward(self):
        functional_inputs = [x for x in self.inputs if x not in self.free_inputs]
        for node in functional_inputs:
            cursor:Node = node
            while cursor.next:
                cursor = cursor.next
                cursor.func()

    def mutate(self, lr):
        p = random.random()
        l = len(self.mids)
        if p<lr:
            if 0 < l < 10:
                self._mutator(p, 0.2, 0.95)
            elif l < 15:
                self._mutator(p, 0.5, 0.98)
            else:
                self._mutator(p, 0.7, 0.99)

    def _mutator(self, p, x, y):
        if p < x:
            if len(self.mids)>0:
                to_remove = random.choice(self.mids)
                to_remove.remove()
        elif p < y:
            to_add = random.choice(self.mids)
            self._insert(to_add)
        else:
            to_add = random.choice(self.free_inputs)
            self._insert(to_add)
