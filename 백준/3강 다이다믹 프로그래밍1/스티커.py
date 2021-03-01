t = int(input())

for i in range(t):
    n = int(input())
    dp = [[0 for i in range(3)] for i in range(n+1)]
    arry_score = []
    for _ in range(2):
        arry_score.append(list(map(int, input().split())))

    for j in range(1,n+1):
        dp[j][0] = max(dp[j-1][0], dp[j-1][1], dp[j-1][2])
        dp[j][1] = max(dp[j-1][0], dp[j-1][2]) + arry_score[0][j-1]
        dp[j][2] = max(dp[j-1][0], dp[j-1][1]) + arry_score[1][j-1]

    print(max(dp[n][0], dp[n][1], dp[n][2]))