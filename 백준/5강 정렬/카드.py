# import sys
# n = int(sys.stdin.readline())
# s = [0 for i in range(n+1)]
# index = 0
# # ans = 0
# for i in range(n):
#     a = int(sys.stdin.readline())
#     s[a] += 1
#     # if s[a] > ans:
#     #     ans = s[a]
# print(s.index(max(s)))
# # print(s.index(ans))

import sys
n = int(sys.stdin.readline())
s = {}
for i in range(n):
    value = int(sys.stdin.readline())
    if value in s:
        s[value] += 1
    else:
        s[value] = 1

dic = sorted(s.items(), key=lambda x: (-x[1],x[0]))
print(dic[0][0])