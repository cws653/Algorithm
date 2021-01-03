# def two_count(x):
#     answer = 0
#     while x % 2 == 0:
#         x /= 2
#         answer += 1
#     return answer
#
# def five_count(x):
#     answer = 0
#     while x % 5 == 0:
#         x /= 5
#         answer += 1
#     return answer
#
# n, m = map(int, input().split())
#
# if m == 0:
#     print(0)
# else:
#     print(min(two_count(n) - two_count(m) - two_count(n-m), five_count(n) - five_count(m) - five_count(n-m)))

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

if m == 0:
    print(0)
else:
    print(min(two_count(n) - two_count(m) - two_count(n-m), five_count(n) - five_count(m) - five_count(n-m)))