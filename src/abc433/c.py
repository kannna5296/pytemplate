t = str(input())
result = 0
for idx, value in enumerate(t):
    if idx + 1 >= len(t):# 最後の行は比較対象がないのでスキップ
        break
    value = int(value)
    nextvalue = int(t[idx+1])
    count = 0
    if (value == nextvalue - 1): # Ni + 1 = Ni+1なところを探す
        count = 1 #見つかった時点で一つ確定
        for increment in range(1, idx+1): #前後に広げていって、それぞれ同じ値だったら文字列とする判定
            target_left_idx = idx - increment
            target_right_idx = idx + 1 + increment
            if target_left_idx < 0 or target_right_idx >= len(t): #範囲内に達したらbreak
                break
            if ((int(t[target_left_idx]) == value) and (int(t[target_right_idx]) == nextvalue)):
                count = count + 1
            else:
                break
        result = result + count
print(result)
