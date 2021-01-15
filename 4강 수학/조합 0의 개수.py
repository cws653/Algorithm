# n,m = map(int, input().split())
# s = n-m
#
# def makeFactorial(x):
#     y = 1
#     for i in range(1, x+1):
#         y *= i
#     return y
# N = makeFactorial(n)
# M = makeFactorial(m)
# S = makeFactorial(s)
#
# first = [0,0]
# second = [0,0]
# third = [0,0]
#
# def countSecond(x):
#     count = 0
#     while x%2 == 0:
#         count += 1
#         x //= 2
#     return count
# def countFifth(x):
#     count = 0
#     while x%5 == 0:
#         count += 1
#         x //= 5
#     return count
#
# first = [countSecond(N), countFifth(N)]
# second = [countSecond(M), countFifth(M)]
# third = [countSecond(S), countFifth(M)]
# print(min(first[0]-second[0]-third[0], first[1]-second[1]-third[1]))

# n,m = map(int, input().split())
#
# def fiveCount(x):
#     y = 0
#     while x%5 == 0:
#         y += x//5
#         x //= 5
#     return y
#
# def secondCount(x):
#     y = 0
#     while x%2 == 0:
#         y += x//2
#         x //= 2
#     return y
#
# if m == 0:
#     print(0)
# else:
#     print(min(secondCount(n)-secondCount(m)-secondCount(n-m), fiveCount(n)-fiveCount(m)-fiveCount(n-m)))

def two_count(x):
    answer = 0
    while x != 0:
        x = x // 2
        answer += x
    return answer

def five_count(x):
    answer = 0
    while x != 0:
        x = x // 5
        answer += x
    return answer

n, m = map(int, input().split())

print(five_count(m))
print(two_count(m))

if m == 0:
    print(0)
else:
    print(min(two_count(n) - two_count(m) - two_count(n-m), five_count(n) - five_count(m) - five_count(n-m)))