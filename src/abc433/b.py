n = int(input())
list = list(map(int, input().split()))

for index, value in enumerate(list):
    if index == 0:
        print("-1")
        continue
    result = "-1"
    for i in range(0, index):
        if value < list[i]:
            result = str(i + 1)
    print(result)
