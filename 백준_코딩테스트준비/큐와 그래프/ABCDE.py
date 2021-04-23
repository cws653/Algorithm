import sys
n,m = map(int, sys.stdin.readline().split())
s = [[] for i in range(n)]
visited = [0 for i in range(n)]
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    s[a].append(b)
    s[b].append(a)

def dfs(x,depth):
    visited[x] = 1
    global ans
    if depth >= 4:
        ans = True
        return
    for i in s[x]:
        if visited[i] == 0:
            dfs(i,depth+1)
            visited[i] = 0

ans = False
for i in range(n):
    dfs(i,0)
    visited[i] = 0
    if ans:
        break
print(1 if ans else 0)