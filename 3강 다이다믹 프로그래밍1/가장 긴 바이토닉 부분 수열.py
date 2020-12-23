n = int(input())
s = list(map(int, input().split()))
d1 = [0 for i in range(n)]
d2 = [0 for i in range(n)]

for i in range(n):
    d1[i] = 1
    for j in range(i):
        if s[j] < s[i] and d1[i] < d1[j] + 1:
            d1[i] = d1[j] + 1

for i in range(n - 1, -1, -1):
    d2[i] = 1
    for j in range(n - 1, i - 1, -1):
        if s[j] < s[i] and d2[i] < d2[j] + 1:
            d2[i] = d2[j] + 1

ans = 0
for i in range(n):
    if ans < d1[i] + d2[i] - 1:
        ans = d1[i] + d2[i] - 1

print(ans)