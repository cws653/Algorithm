import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
s = []
dist = [[-1]*n for i in range(m)]
q = deque()

for i in range(m):
    s.append(sys.stdin.readline().strip())

dx = [1,-1,0,0]
dy = [0,0,1,-1]
dist[0][0] = 0
q.append([0,0])
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if dist[nx][ny] == -1:
                if s[nx][ny] == '0':
                    q.appendleft([nx,ny])
                    dist[nx][ny] = dist[x][y]
                elif s[nx][ny] == '1':
                    q.append([nx,ny])
                    dist[nx][ny] = dist[x][y] + 1

print(dist[m-1][n-1])