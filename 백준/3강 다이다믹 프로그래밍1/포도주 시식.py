# 2차원 배열로 푸는 방
# n = int(input())
# s = [0 for i in range(n+1)]
# d = [[0 for i in range(3)] for i in range(n+1)]
#
# for i in range(1, n+1):
#     s[i] = int(input())
#
# # d[n][0] = max(d[n-1][0], d[n-1][1], d[n-1][2])
# # d[n][1] = d[n-1][0] + s[n]
# # d[n][2] = d[n-1][1] + s[n]
# d[1][0] = s[0]
# d[1][1] = s[1]
# d[1][2] = s[0]
# for i in range(2, n+1):
#     d[i][0] = max(d[i-1][0], d[i-1][1], d[i-1][2])
#     d[i][1] = d[i-1][0] + s[i]
#     d[i][2] = d[i-1][1] + s[i]
#
# print(max(d[n]))

# 1치원 배열로 푸는 방법
n = int(input())
s = [0 for i in range(n+1)]
d = [0 for i in range(n+1)]

for i in range(1, n+1):
    s[i] = int(input())

d[1] = s[1]
d[2] = s[1] + s[2]
for i in range(3, n+1):
    d[i] = d[i-1]
    if d[i] < d[i-2] + s[i]:
        d[i] = d[i-2] + s[i]
    if d[i] < d[i-3] + s[i-1] + s[i]:
        d[i] = d[i-3] + s[i-1] + s[i]

print(d[n])