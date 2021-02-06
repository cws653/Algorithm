import sys
from collections import deque
n,m,v = map(int, sys.stdin.readline().split())
s = [[0 for i in range(n+1)] for i in range(n+1)]
visit = [0 for i in range(n+1)]

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    s[a][b] = 1
    s[b][a] = 1

def dfs(i):
    print(i, end=' ')
    visit[i] = 1
    for j in range(1, n+1):
        if s[i][j] == 1 and visit[j] == 0:
            dfs(j)

def bfs(i):
    visit[i] = 0
    q = deque()
    q.append(i)
    while q:
        a = q.popleft()
        print(a, end=' ')
        for b in range(1,n+1):
            if s[a][b] == 1 and visit[b] == 1:
                q.append(b)
                visit[b] = 0

dfs(v)
print()
bfs(v)
