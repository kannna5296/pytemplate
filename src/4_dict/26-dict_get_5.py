# 投票数のカウントをdictで管理したい。投票者リストで管理。setdefault

votes = {
    "a": ["Bob", "Alice"],
    "b": ["Coco", "Deb"],
}

key = "c"
who = "Emly"
names = votes.setdefault(key, []) #keyがなかった場合に、第二引数をvalueに設定する。また設置したデフォルトを返す
names.append(who)
print(votes)
