import sys
from collections import deque

m,n = map(int, sys.stdin.readline().split())
s = []
queue = deque()

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))

def bfs():
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and s[nx][ny] == 0:
                s[nx][ny] = s[a][b] + 1
                queue.append([nx,ny])
for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            queue.append([i,j])
bfs()
isTrue = False
result = -2
for i in s:
    for j in i:
        if j == 0:
            isTrue = True
        result = max(result, j)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)