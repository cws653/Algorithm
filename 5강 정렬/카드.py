# n = int(input())
# s = [int(input()) for i in range(n)]
# d = [0 for i in range(n)]
# d[0] = s[0]
# sum = 1
# for i in range(1, n):
#     if s[i-1] == s[i]:
#         sum += 1
#         d[i] = sum
#     else:
#         d[i] = sum
#     sum = 1
# print(max(d))

# n = int(input())
# s = [int(input()) for i in range(n)]
# s.sort()
# ans = s[0]
# ans_cnt = 1
# cnt = 1
# for i in range(1, n):
#     if s[i] == s[i-1]:
#         cnt += 1
#     else:
#         cnt = 1
#     if ans_cnt < cnt:
#         ans_cnt = cnt
#         ans = a[i]
# print(ans)

n = int(input())
s = {}
for i in range(n):
    value = int(input())
    if value in s:
        s[value] += 1
    else:
        s[value] = 1
dic = sorted(s.items(), key=lambda x: (-x[1], x[0]))
print(dic[0][0])