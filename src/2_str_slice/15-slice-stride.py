x = ["red", "orange", "yellow", "green", "blue", "purple"]
odds = x[::2]  # 0から始まって1個飛ばし ストライド(増分)指定
evens = x[1::2]  # 1から始まって1個飛ばし
print(odds)
print(evens)

hoge = x[::-2]  # 末尾から始まって1個飛ばし ストライド(増分)指定
print(hoge)

x = ["a", "b", "c", "d", "e", "f", "g", "h"]
fuga = x[-2:2:-2]  # →読みづらいからやめろ
print(fuga)

# これならOK！
y = x[::2]  # index=0から始まって1個飛ばしで取得する　ストライド
print(y)
z = y[1:-1]  # index=1から始まって、index末尾の一個の手前まで　スライス
print(z)
