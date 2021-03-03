import sys
n = int(sys.stdin.readline())
s = []
dp = [[0 for i in range(2)] for i in range(n)]

for i in range(n):
    s.append(int(sys.stdin.readline()))

dp[0][0] = s[0]
dp[1][0] = s[1]
dp[1][1] = s[0] + s[1]
for i in range(2, n):
    dp[i][0] = max(dp[i - 2][0], dp[i - 2][1]) + s[i]
    dp[i][1] = dp[i-1][0] + s[i]

print(max(dp[n-1]))