n = int(input())
a = [int(x) for x in input().split()]
cnt = [[0, 0] for x in range((1 << 20) + 3)]
cnt[0][1] = 1
x = 0
res = 0
for j in range(n):
    x ^= a[j]
    res += cnt[x][j % 2]
    cnt[x][j % 2] += 1
print(res)
