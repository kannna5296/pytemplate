import bisect

# コピペ〜〜

n, m = map(int, input().split())
list = list(map(int, input().split()))
g = [[] for _ in range(11)]  # 空配列が11個ある配列(0桁から10桁それぞれ)
print(g)
for v in list:
    # print(str(v), len(str(v)), v % m)
    g[len(str(v))].append(v % m)
print(g)
for gg in g:
    gg.sort()
print(g)
ans = 0
for ai in list:
    for k in range(1, 11):
        ai = (ai * 10) % m
        key = (m - ai) % m
        ans += bisect.bisect_left(g[k], key + 1) - bisect.bisect_left(g[k], key)
print(ans)
