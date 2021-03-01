n = int(input())
s = list(map(int, input().split()))
# 합을 보여주는 배열
dp = [0 for i in range(n)]

for i in range(n):
    dp[i] = s[i]
    for j in range(i):
        if s[i] > s[j] and dp[i] < dp[j] + s[i]:
            dp[i] = dp[j] + s[i]

print(max(dp))