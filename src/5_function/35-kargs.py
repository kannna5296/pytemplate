def print_args(**kargs):
    for key, value in kargs.items():
        print(f"{key}: {value}")

print_args(hoge=3, ana=4)

def flow_rate(weight_diff, time_diff, period=1): #periodはお＠雨書なる
    return (weight_diff / time_diff) * period

print(f"flow_per_second: {flow_rate(50, 10, period=1)}")
print(f"flow_per_hour: {flow_rate(50, 10, period=3600)}")
print(f"flow_per_second: {flow_rate(50, 10, 1)}") # not better. わかりづらい。key指定した方が良い
