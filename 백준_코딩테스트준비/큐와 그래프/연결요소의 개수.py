import sys
sys.setrecursionlimit(10000)
n,m = map(int, sys.stdin.readline().split())
# graph = [[0]*(n+1) for i in range(n+1)]
graph = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    # graph[b][a] = 1
    # graph[a][b] = 1
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    visited[x] = 1
    for y in graph[x]:
        if visited[y] == 0:
            dfs(y)

ans = 0
for i in range(1,n+1):
    if visited[i] == 0:
        dfs(i)
        ans += 1
print(ans)