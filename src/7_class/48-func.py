def log_missing():
    print("Key added")
    return 0 #初期値が0ってこと！

from collections import defaultdict

current = {"green": 12, "blue":4}
increments = [
    ("red", 5),
    ("blue", 17),
    ("orange", 9),
]
result = defaultdict(
    log_missing, # default_factoryという引数. keyがなかった時のデフォルトの作り方を示す
    current
)
print("before: ", dict(result))
for key, amount in increments:
    result[key] += amount
print("after: ", dict(result))


#print(help(defaultdict))


#関数じゃなくて、

class BetterCountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self):
        print("key added from class")
        self.added=1
        return 0

counter = BetterCountMissing()
result = defaultdict(
    counter, #__call__を実装した(=callableなクラス)を付与することもできる
    current
)
print("before: ", dict(result))
for key, amount in increments:
    result[key] += amount
print("after: ", dict(result))
