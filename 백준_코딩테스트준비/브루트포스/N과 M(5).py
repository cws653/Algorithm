N,M = map(int, input().split())
num_list = list(map(int, input().split()))
visited = [False] * N
num_list.sort()
ans = []
def dfs(depth):
    if depth == M:
        print(*ans)
        return
    for i,v in enumerate(num_list):
        if not visited[i]:
            visited[i] = True
            ans.append(v)
            dfs(depth+1)
            visited[i] = False
            ans.pop()

dfs(0)