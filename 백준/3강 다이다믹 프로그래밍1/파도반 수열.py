# import sys
# t = int(sys.stdin.readline())
#
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     dp = [0 for i in range(n+1)]
#     dp[1],dp[2],dp[3],dp[4],dp[5] = 1,1,1,2,2
#     for i in range(6, n+1):
#         dp[i] = dp[i-1] + dp[i-5]
#     print(dp[n])

t = int(input())
dp = [0 for i in range(101)]
dp[1],dp[2],dp[3],dp[4],dp[5] = 1,1,1,2,2

for i in range(6,101):
    dp[i] = dp[i-1] + dp[i-5]

for i in range(t):
    n = int(input())
    print(dp[n])