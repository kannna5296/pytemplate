x, y, z = map(int, input().split())

year = 0
flg = False
while(True):
    if (x == y * z):
        flg = True
    x = x + 1
    y = y + 1
    year = year + 1
    #print(f"{year}年経過")
    if (y == 120):
        break
if flg:
    print("Yes")
else:
    print("No")
