n, k = map(int, input().split())
d = [[0 for i in range(201)] for i in range(201)]
mod = 1000000000
d[0][0] = 1
for i in range(1, k+1):
    for j in range(n+1):
        for l in range(j+1):
            d[j][i] += d[j-l][i-1]

print(d[n][k] % mod)
