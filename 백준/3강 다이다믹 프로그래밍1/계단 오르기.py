n = int(input())
s = []
d = [[0 for i in range(2)] for i in range(n)]

for i in range(n):
    s.append(int(input()))

# d[i][0] = d[i-2][0] + d[i-2][1] + s[i]
# d[i][1] = d[i-1][0] + s[i]

d[0][0] = s[0]
d[1][0] = s[1]
d[1][1] = s[0] + s[1]

for i in range(2, n):
    d[i][0] = max(d[i-2][0], d[i-2][1]) + s[i]
    d[i][1] = d[i-1][0] + s[i]

print(max(d[n-1]))