# n = int(input())
# ans = 0
#
# for i in range(2, n+1):
#     while n%5 == 0:
#         ans += 1
#         n /= 5
#
# print(ans)

n = int(input())
print(n//5 + n//25 + n//125)