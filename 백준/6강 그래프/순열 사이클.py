import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    visit[x] = 1
    y = s[x]
    if visit[y] == 0:
        dfs(y)

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    s = [0] + list(map(int, sys.stdin.readline().split()))
    visit = [0 for i in range(n+1)]
    cnt = 0
    for i in range(1, n+1):
        if visit[i] == 0:
            dfs(i)
            cnt += 1
    print(cnt)

