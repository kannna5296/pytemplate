# 投票数のカウントをdictで管理したい

counters = {
    "pumpernickel": 2,
    "sourdough": 1,
}

key = "wheat"

# 1例（真面目に分岐）
# if key in counters:
#     count = counters[key]
# else:
#     count = 0
# counters[key] = count + 1


# 2例（例外で分岐
# try:
#     count = counters[key]
# except KeyError:
#     count = 0
# counters[key] = count + 1

# getだとkeyなかった時のデフォルト値を置けるので、簡便にかける！！
count = counters.get(key, 0)
counters[key] = count + 1


print(counters)
