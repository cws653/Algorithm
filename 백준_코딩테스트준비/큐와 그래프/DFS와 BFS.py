import sys
from collections import deque
n,m,v = map(int, sys.stdin.readline().split())
graph = [[0]*(n+1) for i in range(n+1)]
visited = [0 for i in range(n+1)]
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(x):
    visited[x] = 1
    print(x, end = ' ')
    for i in range(1, n+1):
       if graph[x][i] == 1 and visited[i] == 0:
           dfs(i)

def bfs(x):
    visited[x] = 0
    q = deque([x])
    while q:
        a = q.popleft()
        print(a, end = ' ')
        for i in range(1,n+1):
            if visited[i] == 1 and graph[a][i] == 1:
                q.append(i)
                visited[i] = 0

# ans1 = []
# ans2 = []
#
# dfs(v)
# bfs(v)
# print(ans1)
# print(ans2)

dfs(v)
print()
bfs(v)
