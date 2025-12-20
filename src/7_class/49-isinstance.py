class Integer:
    def __init__(self, value):
        self.value = value


class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Multiply:
    def __init__(self, left, right):
        self.left = left
        self.right = right


tree = Add(Integer(2), Integer(9))  # AST 抽象構文木 abstract syntac tree


# ツリーウォーキング
def evaluate(node):
    if isinstance(node, Integer):
        return node.value
    elif isinstance(node, Add):
        return evaluate(node.left) + evaluate(node.right)
    elif isinstance(node, Multiply):
        return evaluate(node.left) * evaluate(node.right)
    else:
        raise NotImplementedError


print(evaluate(tree))
