n = int(input())
s = list(map(int, input().split()))
d = [0 for i in range(n)]

for i in range(n):
    d[i] = 1
    for j in range(i):
        if s[i] < s[j] and d[i] < d[j] + 1:
            d[i] = d[j] + 1

print(max(d))