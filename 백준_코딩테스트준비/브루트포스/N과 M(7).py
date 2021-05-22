N,M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
visited = [False] * N
ans = []

def dfs(depth):
   if depth == M:
       print(*ans)
       return
   for i,v in enumerate(num_list):
       ans.append(v)
       dfs(depth+1)
       ans.pop()

dfs(0)