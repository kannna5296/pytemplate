import pickle
from functools import wraps


def trace(func):
    @wraps(func)  # wrapper関数を使うときは、functoolsを使うべきよ〜〜
    def wrapper(*args, **kargs):
        args_repr = repr(args)
        kargs_repr = repr(kargs)
        result = func(*args, **kargs)
        print(f"{func.__name__}({args_repr}, {kargs_repr}) -> {result!r}")
        return result

    return wrapper


@trace
def fibonacci(n):
    "n番目のfibonacci数を返す"
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


fibonacci(4)
# help(fibonacci)
print(pickle.dumps(fibonacci))
