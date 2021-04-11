import sys
n,m,v = map(int, sys.stdin.readline().split())
s = [[0]*(n+1) for i in range(n+1)]
visit = [0 for i in range(n+1)]

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    s[a][b] = 1
    s[b][a] = 1

def dfs(x):
    print(x, end=' ')
    visit[x] = 1
    for i in range(1, n+1):
        if visit[i] == 0 and s[x][i] == 1:
            dfs(i)

def bfs(x):
    visit[x] = 0
    queue = [x]
    while queue:
        x = queue.pop(0)
        print(x, end=' ')
        for i in range(1,n+1):
            if visit[i] == 1 and s[x][i] == 1:
                queue.append(i)
                visit[i] = 0

dfs(v)
print()
bfs(v)