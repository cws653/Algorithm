# n = int(input())
#
# N = 1
# for i in range(1, n+1):
#     N *= i
#
# second = 0
# fifth = 0
# while N%2 == 0:
#     second += 1
#     N //= 2
# while N%5 == 0:
#     fifth += 1
#     N //= 5
# print(min(second,fifth))

n = int(input())
print(n//5 + n//25 + n//125)