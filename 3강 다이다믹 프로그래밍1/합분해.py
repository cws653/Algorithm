n, k = map(int, input().split())
d = [[0 for i in range(201)] for j in range(201)]

for i in range(201):
    d[i][1] = 1
for i in range(1, 201):
    for j in range(201):
        for l in range(j+1):
            d[j][i] += d[l][i-1]
print(d[n][k] % 1000000000)
