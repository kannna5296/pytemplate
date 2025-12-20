import functools

# あんま良さがわからんかったかも...

@functools.singledispatch
def my_print(value):
    raise NotImplementedError

@my_print.register(int)
def _(value):
    print("Integer!", value)

@my_print.register(float)
def _(value):
    print("Float!", value)

my_print(3)
my_print(3.0)
