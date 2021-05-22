N,M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
visitied = [False] * N
ans = []

def dfs(depth, idx):
    if depth == M:
        print(*ans)
        return
    for i in range(idx, len(num_list)):
        if not visitied[i]:
            visitied[i] = True
            ans.append(num_list[i])
            dfs(depth+1, i)
            visitied[i] = False
            ans.pop()

dfs(0, 0)