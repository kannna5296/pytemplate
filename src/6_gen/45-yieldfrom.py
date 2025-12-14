# ジェネレータ
def move(period, speed):
    for _ in range(period):
        yield speed


# ジェネレータ
def pause(delay):
    for _ in range(delay):
        yield 0


def animate():
    for delta in move(4, 5):
        yield delta
    for delta in pause(3):
        yield delta
    for delta in move(2, 3):
        yield delta


def render(delta):
    print(f"Delta: {delta}")


def run(func):
    for delta in func():
        render(delta)


print("yieldそのもので書くパターン。")
run(animate)


# ネストされた複数のジェネレータを単一の結合されたジェネレータとして構成できるし読みやすい
def animate_composed():
    yield from move(4, 5)
    yield from pause(3)
    yield from move(2, 3)


print("yieldそのもので書くパターン。")
run(animate_composed)
