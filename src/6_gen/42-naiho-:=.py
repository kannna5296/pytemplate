# 在庫数
stock = {
    "a": 126,
    "b": 121,
    "c": 125,
    "d": 1272,
}

# 注文入った
order = ["a","c"]

def get_batches(count, size):
    '''sizeの塊が何セットできるかを確認する'''
    return count // size

# result = {}
# for name in order:
#     count = stock.get(name,0)
#     batches = get_batches(count,8)
#     if batches:
#         result[name] = batches

##↕一緒
result = {
    name: get_batches(stock.get(name,0),8)
    for name in order
    if get_batches(stock.get(name,0),8)
}
print(result)

## 同じ記法が出てきて冗長...だから、:=(代入式)を使う

result = {
    name: batches for name in order if (batches := get_batches(stock.get(name,0),8))
}
print(result)
