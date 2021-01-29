import sys
sys.setrecursionlimit(10000)
n,m = map(int, sys.stdin.readline().split())
s = [[0 for i in range(n+1)] for i in range(n+1)]
visit = [0 for i in range(n+1)]
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    s[a][b] = 1
    s[b][a] = 1

def dfs(x):
    visit[x] = 1
    for i in range(1, n+1):
        if visit[i] == 0 and s[x][i] == 1:
            dfs(i)

cnt = 0
for i in range(1, n+1):
    if visit[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)