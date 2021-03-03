# n = int(input())
# s = list(map(int, input().split()))
# dp = [0 for i in range(n)]
# dp[0] = s[0]
# ans = s[0]
# for i in range(1,n):
#     if s[i] + dp[i-1] > 0:
#         dp[i] = s[i] + dp[i-1]
#     else:
#         dp[i] = s[i]
#
#     if ans < dp[i]:
#         ans = dp[i]
#     # print(ans)
#
# print(ans)

n = int(input())
s = list(map(int, input().split()))
dp = [0 for i in range(n)]

for i in range(n):
    dp[i] = s[i]
    if i == 0:
        continue
    if dp[i] < dp[i-1] + s[i]:
        dp[i] = dp[i-1] + s[i]

# print(dp)
print(max(dp))