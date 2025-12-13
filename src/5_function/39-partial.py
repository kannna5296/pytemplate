import functools
import math


def log_sum(log_total, value):
    '''
    第一引数にeを底とした第二引数の対数を足し合わせて返却する

    :param log_total: 説明
    :param value: 説明
    '''
    log_value = math.log(value)
    return log_total + log_value

print(log_sum(10,math.e**2))

result = functools.reduce(log_sum, [10,20,40], 0) # 関数,配列,初期値
# loge10 + loge20 + loge40 = loge(10*20*40)

print(math.exp(result))
#eのloge(10*20*40)は10*20*40になるはずなので、8000


####### 例えばこういう関数があった時
def log_sum_alt(value, log_total):
    log_value = math.log(value)
    return log_total + log_value

# 問題は
# ・reduceで使いたいが、reduceは[関数, リスト, int]の順で指定することを期待する
#   なので、reduce[logn_sum_alt, [10,20,30], 0]とかしたい
# ・一方、関数は[int, リスト]の順を期待しているので、リストとintの順が違う

# lambda式で無理やりint, リストの純で受け取る関数を作る
result = functools.reduce(
    lambda total, value: log_sum_alt(total, value) # ここで入れ替える。
    [10,20,40], # 後から引数を渡す
    0
)
# ↑こういう「引数として、関数Aとその関数Aの引数が並ぶ」みたいなことはあるあるらしい
# 一部の引数を固定して、残りの引数を通常通り渡せるようにする、は関数型プログラミングでは一般的らしい（部分適用、カリー化？
# →これをするのがpartialらしい

# partial は「同じ操作だけど一部の条件が違う」ような新しい関数を定義するためのツールです。
# reduce は「複数のデータを集めて一つの結果にする」ためのツールです。

#######または、メンテしてて第一引数が増えた場合

def logn_sum(base, logn_total, value):
    logn_value = math.log(base, value)
    return logn_total + logn_value


result = functools.reduce(
    lambda total, value: logn_sum(10, total, value) # ここで入れ替える。
    [10,20,40], # 後から引数を渡す
    0
)

# こういう「一部引数だけ固定して後から引数追加して良い書き方」をlambda式使わずともかける書き方

result = functools.reduce(
    functools.partial(log_sum, 10),
    [10, 20, 40],
    0
)
