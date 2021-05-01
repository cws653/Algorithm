import sys
from collections import deque
m,n = map(int, sys.stdin.readline().split())
s = []
for i in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))

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
            if 0 <= nx < n and 0 <= ny < m and s[nx][ny] == 0:
                q.append([nx,ny])
                s[nx][ny] = s[a][b] + 1

for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            bfs(i,j)

ans = -2
isTrue = False
for i in s:
    for j in i:
        if j == 0:
            isTrue = True
        ans = max(ans, j)

if isTrue == True:
    print(-1)
elif ans == -1:
    print(0)
else:
    print(ans - 1)