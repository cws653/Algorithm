N,M = map(int, input().split())
visitied = [False] * N
num_list = [i+1 for i in range(N)]
ans = []

def dfs(depth):
    if depth == M:
        print(*ans)
        return
    for i in range(N):
        if not visitied[i]:
            visitied[i] = True
            ans.append(num_list[i])
            dfs(depth+1)
            ans.pop()

            for j in range(i+1, N):
                visitied[j] = False

dfs(0)