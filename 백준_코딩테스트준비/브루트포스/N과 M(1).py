N,M = map(int, input().split())
visited = [False] * N
out = []

def dfs(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            dfs(depth+1, N, M)
            visited[i] = False
            out.pop()

dfs(0, N, M)