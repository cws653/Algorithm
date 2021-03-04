n = int(input())
dp = [0 for i in range(n+1)]
dp[0] = 1
for i in range(2,n+1,2):
    dp[i] = 3*dp[i-2]
    for j in range(i-4, -1, -2):
        dp[i] += dp[j]*2

print(dp[n])