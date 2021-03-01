n = int(input())
# n개의 길이의 이친수의 개수 (경우의수)
dp = [0] * (91)
dp[1] = 1
dp[2] = 1
for i in range(3,91):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])