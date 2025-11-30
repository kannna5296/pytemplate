# 投票数のカウントをdictで管理したい。投票者リストで管理。get使う版

votes = {
    "a": ["Bob", "Alice"],
    "b": ["Coco", "Deb"],
}

key = "c"
who = "Emly"
names = votes.get(key)
if names is None:
    votes[key] = names = []
names.append(who)

print(votes)
