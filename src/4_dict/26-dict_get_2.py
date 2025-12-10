# 投票数のカウントをdictで管理したい。投票者リストで管理。

votes = {
    "a": ["Bob", "Alice"],
    "b": ["Coco", "Deb"],
}

key = "c"
who = "Emly"
if key in votes:
    names = votes[key]
else:
    votes[key] = names = []  # こんな書き方できるんすね〜〜。
    # ⇩これと一緒。votesにkeyvalueを一つ追加するのと、names変数定義を両方する
    # names = []
    # votes[key] = names
    print(names)
    print(votes)
names.append(who)


print(votes)
