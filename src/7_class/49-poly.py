class Node:
    def evaluate(self):
        raise NotImplementedError

    def pretty(self):
        raise NotImplementedError

class IntergerNode(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

    def pretty(self):
        return repr(self.value)

class AddNode(Node):
    def __init__(self, right: Node, left: Node):
        self.left = left
        self.right = right

    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()

    def pretty(self):
        return f"{self.left.pretty()} + {self.right.pretty()}"

class MultiplyNode(Node):
    def __init__(self, right: Node, left: Node):
        self.left = left
        self.right = right

    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()

    def pretty(self):
        return f"({self.left.pretty()}) * ({self.right.pretty()})"


tree = MultiplyNode(
    AddNode(IntergerNode(3), IntergerNode(5)),
    AddNode(IntergerNode(2), IntergerNode(4)),
)


print(f"{tree.pretty()} = {tree.evaluate()}")

