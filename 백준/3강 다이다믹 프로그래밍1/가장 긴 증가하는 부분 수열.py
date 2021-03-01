n = int(input())
s = list(map(int, input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if s[j] < s[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))