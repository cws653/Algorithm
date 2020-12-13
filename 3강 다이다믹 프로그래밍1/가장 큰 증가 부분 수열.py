n = int(input())
a = list(map(int, input().split()))
d = [0 for i in range(n)]

for i in range(0, n):
    d[i] = a[i]
    for j in range(0, i):
        if a[j] < a[i] and d[j] + a[i] > d[i]:
            d[i] = d[j] + a[i]

ans = max(d)
print(ans)