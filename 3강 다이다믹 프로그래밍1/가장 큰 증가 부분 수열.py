n = int(input())
s = list(map(int, input().split()))
d = [0 for i in range(n)]

for i in range(n):
    d[i] = s[i]
    for j in range(i):
        if s[j] < s[i] and d[i] < d[j] + s[i]:
            d[i] = d[j] + s[i]

print(max(d))