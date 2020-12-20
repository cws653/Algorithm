t = int(input())

for i in range(t):
    n = int(input())
    s = []
    d = [[0 for i in range(3)] for i in range(n+1)]
    for j in range(2):
        s.append(list(map(int, input().split())))
    # d[n][0] = max(d[n-1][0], d[n-1][1], d[n-1][2])
    # d[n][1] = max(d[n-1][0], d[n-1][2]) + s[0][n]
    # d[n][2] = max(d[n-1][0], d[n-1][1]) + s[1][n]
    # 최종답 = max(d[n][0], d[n][1], d[n][2])
    d[0][0] = d[0][1] = d[0][2] = 0
    # d[1][0] = d
    # d[1][1] = s[0][1]
    # d[1][2] = s[0][2]
    for k in range(1, n+1):
        d[k][0] = max(d[k-1][0], d[k-1][1], d[k-1][2])
        d[k][1] = max(d[k-1][0], d[k-1][2]) + s[0][k-1]
        d[k][2] = max(d[k-1][0], d[k-1][1]) + s[1][k-1]
        # for l in range(3):
        #     if l == 0:
        #         d[k][0] = max(d[k-1][0], d[k-1][1],d[k-1][2])
        #     elif l == 1:
        #         d[k][1] = max(d[k-1][0], d[k-1][2]) + s[0][k-1]
        #     elif l == 2:
        #         d[k][2] = max(d[k-1][0], d[k-1][1]) + s[1][k-1]
    print(max(d[n][0], d[n][1], d[n][2]))
