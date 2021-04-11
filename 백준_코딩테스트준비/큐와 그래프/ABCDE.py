import sys
n,m = map(int, sys.stdin.readline().split())
s = [[] for i in range(n)]
visit = [False for i in range(n)]

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    s[a].append(b)
    s[b].append(a)

def dfs(v, depth):
    global ans
    visit[v] = True
    if depth >= 4:
        ans = True
        return
    for i in s[v]:
        if not visit[i]:
            dfs(i, depth + 1)
            visit[i] = False

ans = False
for i in range(n):
    dfs(i,0)
    visit[i] = False
    if ans:
        break

print(1 if ans else 0)

