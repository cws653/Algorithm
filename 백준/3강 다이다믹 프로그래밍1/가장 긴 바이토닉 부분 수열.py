n = int(input())
s = list(map(int, input().split()))
dp1 = [0 for i in range(n)]
# dp2 = [0 for i in range(n)]
dp3 = [0 for i in range(n)]

for i in range(n):
    dp1[i] = 1
    for j in range(i):
        if s[i] > s[j] and dp1[i] < dp1[j] + 1:
            dp1[i] = dp1[j] + 1

# for i in range(n):
#     dp2[i] = 1
#     for j in range(i):
#         if s[j] > s[i] and dp2[i] < dp2[j] + 1:
#             dp2[i] = dp2[i] + 1

for i in range(n-1, -1, -1):
    dp3[i] = 1
    for j in range(n-1, i, -1):
        if s[i] > s[j] and dp3[i] < dp3[j] + 1:
            dp3[i] = dp3[j] + 1

# print(dp1)
# print(dp2)
# print(dp3)
ans = 0
for i in range(n):
    if ans < dp1[i] + dp3[i] - 1:
        ans = dp1[i] + dp3[i] - 1

print(ans)