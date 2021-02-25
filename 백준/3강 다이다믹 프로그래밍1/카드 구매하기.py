# 이 문제는 로직 이해는 할 수 있으나 밑에 for문을 생각하는게 어려울 것이라 생각된다.
n = int(input())
dp = [0] * (n+1)
p = [0] + list(map(int, input().split()))
dp[1] = p[1]
for i in range(2,n+1):
    for j in range(1,i+1):
        if dp[i] < dp[i-j] + p[j]:
            dp[i] = dp[i-j] + p[j]
print(dp[n])