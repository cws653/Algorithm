n,m,v = map(int, input().split())
s = [[0 for i in range(n+1)] for i in range(n+1)]
visit = [0 for i in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    s[a][b] = 1
    s[b][a] = 1

def dfs(v):
    visit[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if visit[i] == 0 and s[v][i] == 1:
            visit[i] = 1
            dfs(i)

def bfs(v):
    queue = [v]
    visit[v] = 0
    while(queue):
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, n+1):
            if visit[i] == 1 and s[v][i] == 1:
                queue.append(i)
                visit[i] = 0

dfs(v)
print()
bfs(v)