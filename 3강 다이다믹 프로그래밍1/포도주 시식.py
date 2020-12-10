n = int(input())
s = []
# d = [[0 for i in range(n)] for j in range(3)]
d = [0 for i in range(n)]

for i in range(n):
    s.append(int(input()))

d[0] = s[0]
d[1] = s[0] + s[1]

for i in range(2, n):
    # 0번 연속해서 마신 포도주
    d[i] = d[i-1]
    if d[i] < d[i-2] + s[i]:
        d[i] = d[i-2] + s[i]
    if d[i] < d[i-3] + s[i] + s[i-1]:
        d[i] = d[i-3] + s[i] + s[i-1]

print(d[n-1])