car_ages = [0, 9, 4, 8, 76, 20, 19, 1, 6, 15]
de = sorted(car_ages)
print(de)

# NG
# oldest, second_oldest = de

# not better
# oldest = de[0]
# second_oldes = de[1]
# other = de[2:]
# いけるけど、読みづらい

# 読みやすい！
oldest, second_oldest, *others = de
print(oldest)
print(second_oldest)
print(others)


# *変数は最後じゃなくてOK！
oldest, *others, youngest = de
print(oldest)
print(others)
print(youngest)

# あんパックは一度に1回まで
# oldest, *middle, *middle2, yougest = de
