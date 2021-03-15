n,k = map(int, input().split())
dp = [[0 for i in range(201)] for i in range(201)]
dp[0][0] = 1
mod = 1000000000
for i in range(1, k+1):
    for j in range(n+1):
        for l in range(j+1):
            dp[j][i] += dp[j-l][i-1]

print(dp[n][k] % mod)