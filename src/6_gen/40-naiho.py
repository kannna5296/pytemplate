a = [1,2,3,4,5]

sq = [x**2 for x in a]
print(sq)
print(type(sq))

sq = [x**2 for x in a if x%2 == 0]
print(sq)
print(type(sq))

sq = {x: x**2 for x in a} #辞書にする
print(sq)
print(type(sq))


sq = {x**2 for x in a} #setにする
print(sq)
print(type(sq))

#filter,mapもあるけど、可読性が低くなる
#リストそのものを生成しないので、メモリを節約したい場合はfilter,map使うのもありでOK
