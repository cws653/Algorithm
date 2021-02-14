import sys
from collections import deque

n = int(sys.stdin.readline())
s = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
q = deque()
cnt = 1

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs1(x,y,cnt):
    visit[x][y] = cnt
    q.append([x,y])
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if s[nx][ny] == 1 and visit[nx][ny] == 0:
                    visit[nx][ny] = cnt
                    q.append([nx, ny])

def bfs2(num):
    while q2:
        a,b = q2.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visit[nx][ny] != num and s[nx][ny] == 1:
                    return visit2[a][b] - 1
                if visit2[nx][ny] == 0 and s[nx][ny] == 0:
                    q2.append([nx,ny])
                    visit2[nx][ny] += visit2[a][b] + 1

for i in range(n):
    for j in range(n):
        if s[i][j] == 1 and visit[i][j] == 0:
            bfs1(i,j,cnt)
            cnt += 1

ans = sys.maxsize
for k in range(1, cnt):
    q2 = deque()
    visit2 = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if s[i][j] == 1 and visit[i][j] == k:
                q2.append([i, j])
                visit2[i][j] = 1
    result = bfs2(k)
    ans = min(ans, result)

print(ans)