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
    a = [] # 3가지 경우의 수의 합을 나타내는 배
    n = int(input()) # 열의 개
    for k in range(2):
        s.append(list(map(int, input().split())))수
        # 큰 배열의 인덱스는 행의값, 작은 배열의 인덱스는 열값이라고 생각하면 된다.
    a = [[0 for i in range(1)] for j in range(3)]열
    for j in range()

print(a)