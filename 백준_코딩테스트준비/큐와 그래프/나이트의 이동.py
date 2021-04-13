from collections import deque
import sys
k = int(input())
queue = deque()

dx = [-2,-2,-1,1,2,2,1,-1]
dy = [-1,1,2,2,1,-1,-2,-2]

def bfs(nx, ny, ax, ay):
    queue.append([nx,ny])
    s[nx][ny] = 1
    while queue:
        a,b = queue.popleft()
        if a == ax and b == ay:
            print(s[a][b] - 1)
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and s[x][y] == 0:
                queue.append([x,y])
                s[x][y] = s[a][b] + 1

for i in range(k):
    n = int(input())
    nx, ny = map(int, input().split())
    ax, ay = map(int, input().split())
    s = [[0]*n for i in range(n)]
    bfs(nx, ny, ax, ay)


