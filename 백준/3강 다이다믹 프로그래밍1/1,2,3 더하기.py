# import sys
# t = int(sys.stdin.readline())
#
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     dp = [0 for _ in range(n+1)]
#     dp[0], dp[1], dp[2] = 1, 1, 2
#     for i in range(3, n+1):
#         dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
#     print(dp[n])

import sys
t = int(sys.stdin.readline())
dp = [0 for _ in range(11)]
dp[0], dp[1], dp[2] = 1,1,2
for i in range(3,11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for i in range(t):
    n = int(sys.stdin.readline())
    print(dp[n])