N,M = map(int, input().split())
num_list = [i+1 for i in range(N)]
ans = []

def dfs(depth):
    if depth == M:
        print(*ans)
        return
    for i in range(N):
        ans.append(num_list[i])
        dfs(depth+1)
        ans.pop()

dfs(0)