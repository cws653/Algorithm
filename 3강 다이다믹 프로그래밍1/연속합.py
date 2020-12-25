n = int(input())
s = list(map(int, input().split()))
d = [0 for i in range(n)]

for i in range(n):
    d[i] = s[i]
    if i == 0:
        continue
    if d[i] < d[i-1] + s[i]:
        d[i] = d[i-1] + s[i]

print(max(d))