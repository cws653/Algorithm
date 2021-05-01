import sys
from collections import deque
n = int(sys.stdin.readline())
s = []
cnt = []
for i in range(n):
    s.append(list(map(int, sys.stdin.readline().strip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    s[x][y] = 0
    count = 1
    q = deque()
    q.append([x,y])
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and s[nx][ny] == 1:
                q.append([nx, ny])
                s[nx][ny] = 0
                count += 1
    return count

for i in range(n):
    for j in range(n):
        if s[i][j] == 1:
            cnt.append(bfs(i,j))
cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)