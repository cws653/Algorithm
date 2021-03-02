# n = int(input())
# s = list(map(int, input().split()))
# dp1 = [0 for i in range(n)]
# dp2 = [0 for i in range(n)]
#
# for i in range(n):
#     dp1[i] = 1
#     for j in range(i):
#         if s[i] > s[j] and dp1[i] < dp1[j] + 1:
#             dp1[i] = dp1[j] + 1
#
# a = dp1.index(max(dp1))
# for i in range(a, n):
#     dp2[i] = 1
#     for j in range(i):
#         if s[j] > s[i] and dp2[i] < dp2[j] + 1:
#             dp2[i] = dp2[j] + 1
#
# print(max(dp1) + max(dp2) - 1)

n = int(input())
s = list(map(int, input().split()))
d1 = [0 for i in range(n)]
d2 = [0 for i in range(n)]

for i in range(n):
    d1[i] = 1
    for j in range(i):
        if s[j] < s[i] and d1[i] < d1[j] + 1:
            d1[i] = d1[j] + 1

for i in range(n - 1, -1, -1):
    d2[i] = 1
    for j in range(n - 1, i - 1, -1):
        if s[j] < s[i] and d2[i] < d2[j] + 1:
            d2[i] = d2[j] + 1

ans = 0
for i in range(n):
    if ans < d1[i] + d2[i] - 1:
        ans = d1[i] + d2[i] - 1

print(ans)