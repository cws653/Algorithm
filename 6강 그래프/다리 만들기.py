import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):
    global cnt
    visit[x][y] = 1
    graph[x][y] = cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visit[nx][ny] == 0 and graph[nx][ny]:
                dfs(nx, ny)

def bfs(z):
    global ans
    dist = [[-1]*n for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(n):
            if graph[i][j] == z:
                queue.append([i,j])
                dist[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > 0 and graph[nx][ny] != z:
                    ans = min(ans, dist[x][y])
                    return
                if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append([nx, ny])

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
cnt = 1
ans = sys.maxsize
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visit[i][j] == 0:
            dfs(i,j)
            cnt += 1

for i in range(1, cnt):
    bfs(i)

print(ans)