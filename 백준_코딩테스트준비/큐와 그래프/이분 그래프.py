import sys

def bfs(v, visited, color):
    q = [v]
    visited[v] = True
    color[v] = 1
    while q:
        now = q.pop(0)
        for nxt in s[now]:
            if not visited[nxt]:
                q.append(nxt)
                color[nxt] = 3 - color[now]
                visited[nxt] = True
            else:
                if color[now] == color[nxt]:
                    return False
    return True

k = int(sys.stdin.readline())
for _ in range(k):
    v,e = map(int, sys.stdin.readline().split())
    s = [[] for i in range(v+1)]
    visited = [False for i in range(v+1)]
    color = [0 for i in range(v+1)]
    flag = True

    for i in range(e):
        a,b = map(int, sys.stdin.readline().split())
        s[a].append(b)
        s[b].append(a)

    for i in range(1, v+1):
        if not visited[i]:
            if not bfs(i, visited, color):
                flag = False
                break
    if not flag:
        print("NO")
    else:
        print("YES")
