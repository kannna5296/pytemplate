def my_func(items: list[str]) -> None:
    items.append(4)


x = [1, 2, 3]
my_func(x)
print(x)

print("### list型の場合 ###")
# 実際は、参照の値渡し、らしい
a = [7, 6, 5]
b = a
print(f"my_func前 {a}, {b}")
my_func(b)
print(f"my_func後 {a}, {b}")

print("### int型の場合 ###")


def func(arg):
    arg = arg * 2


aa = 1
func(aa)
print(aa)
