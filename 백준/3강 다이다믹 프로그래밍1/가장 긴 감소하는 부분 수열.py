# n = int(input())
# s = list(map(int, input().split()))
# dp = [0 for i in range(n)]
#
# for i in range(n):
#     dp[i] = 1
#     for j in range(i):
#         if s[i] < s[j] and dp[i] < dp[j] + 1:
#             dp[i] = dp[j] + 1
#
# print(max(dp))

n = int(input())
s = list(map(int, input().split()))
dp = [0 for i in range(n)]

for i in range(n - 1, -1, -1):
    dp[i] = 1
    for j in range(n - 1, i, -1):
        if s[j] < s[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))