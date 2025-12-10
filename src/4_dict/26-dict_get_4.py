# 投票数のカウントをdictで管理したい。投票者リストで管理。セイウチ演算子版。あんま好きではない

votes = {
    "a": ["Bob", "Alice"],
    "b": ["Coco", "Deb"],
}

key = "c"
who = "Emly"
if names := votes.get(key) is None:  # names代入と、namesの値に対するif文を一気にやる
    votes[key] = names = []
names.append(who)
print(votes)
