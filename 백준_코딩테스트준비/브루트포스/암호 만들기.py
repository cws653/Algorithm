def dfs(depth, idx):
    if depth == l:
        vo = 0
        co = 0
        for i in range(l):
            if ans[i] in 'aeiou':
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print(''.join(ans))
        return
    for i in range(idx, c):
        if not visited[i]:
            visited[i] = True
            ans.append(arr[i])
            dfs(depth+1, i+1)
            visited[i] = False
            ans.pop()

l,c = map(int, input().split())
visited = [False for i in range(c)]
arr = input().split()
arr.sort()
ans = []
dfs(0,0)
