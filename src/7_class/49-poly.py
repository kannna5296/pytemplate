class Node:
    def evaluate(self):
        raise NotImplementedError

class IntergerNode(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

class AddNode(Node):
    def __init__(self, right: Node, left: Node):
        self.left = left
        self.right = right

    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()

class MultiplyNode(Node):
    def __init__(self, right: Node, left: Node):
        self.left = left
        self.right = right

    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()


tree = MultiplyNode(
    AddNode(IntergerNode(3), IntergerNode(5)),
    AddNode(IntergerNode(2), IntergerNode(4)),
)

print(tree.evaluate())

