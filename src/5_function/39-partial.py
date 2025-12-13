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
