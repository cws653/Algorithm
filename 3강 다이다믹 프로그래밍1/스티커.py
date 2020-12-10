# t = int(input())
# for i in range(t):
#     s = []
#     n = int(input())
#     for k in range(2):
#         s.append(list(map(int, input().split())))
#     s[0][1] += s[1][0]
#     s[1][1] += s[0][0]
#     for j in range(2, n):
#         s[0][j] += max(s[1][j - 1], s[1][j - 2])
#         s[1][j] += max(s[0][j - 1], s[0][j - 2])
#     print(s)
#     print(max(s[0][n - 1], s[1][n - 1]))

t = int(input())

for i in range(t):
    s = [] # 초기 숫자 입력값을 담은 배열
    a = [] # 3가지 경우의 수의 합을 나타내는 배열
    n = int(input()) # 열의 개
    for k in range(2):
        s.append(list(map(int, input().split())))

    a = [[0 for i in range(n + 1)] for j in range(3)]
    a[0][0] = a[1][0] = a[2][0] = 0
    for j in range(1, n+1):
        a[0][j] = max(a[0][j-1], a[1][j-1], a[2][j-1])
        a[1][j] = max(a[0][j-1], a[2][j-1]) + s[0][j-1]
        a[2][j] = max(a[0][j-1], a[1][j-1]) + s[1][j-1]
    answear = 0
    for j in range(1, n+1):
        answear = max(answear,a[0][j],a[1][j],a[2][j])
    print(answear)

