import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
s = []
for i in range(n):
    s.append(list(map(int, sys.stdin.readline().strip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append([x,y])
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and s[nx][ny] == 1:
                q.append([nx, ny])
                s[nx][ny] = s[a][b] + 1

for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            bfs(i,j)

print(s[n-1][m-1])