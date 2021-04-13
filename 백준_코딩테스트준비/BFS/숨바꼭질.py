# from collections import deque
# import sys
# n,k = map(int, sys.stdin.readline().split())
# visited = [0 for i in range(100001)]
# queue = deque()
# queue.append([n,0])
# while queue:
#     start, depth = queue.popleft()
#     if start == k:
#         break
#     visited[start] = 1
#     if start - 1 >= 0 and visited[start - 1] == 0:
#         queue.append([start - 1, depth + 1])
#     if start + 1 <= 100000 and visited[start + 1] == 0:
#         queue.append([start + 1, depth + 1])
#     if start * 2 <= 100000 and visited[start * 2] == 0:
#         queue.append([start * 2, depth + 1])
# print(queue[0][1])

from collections import deque

def bfs(v):
    count = 0
    q = deque([[v, count]])
    while q:
        v = q.popleft()
        e = v[0]
        count = v[1]
        if not visited[e]:
            visited[e] = True
            if e == K:
                return count
            count += 1
            if (e * 2) <= 100000:
                q.append([e * 2, count])
            if (e + 1) <= 100000:
                q.append([e + 1, count])
            if (e - 1) >= 0:
                q.append([e - 1, count])
    return count


N, K = map(int, input().split())
visited = [False] * 100001
print(bfs(N))