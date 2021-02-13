import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
s = []
for _ in range(n):
    s.append(list(map(int, sys.stdin.readline().strip())))

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    s[x][y] = 1
    q = deque()
    q.append([x,y])
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and s[nx][ny] == 1:
                q.append([nx,ny])
                s[nx][ny] = s[a][b] + 1

bfs(0,0)
print(s[n-1][m-1])

# import sys
# n, m = map(int, sys.stdin.readline().split())
# s = []
# for i in range(n):
#     s.append(list(sys.stdin.readline()))
#
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
#
# def bfs(i,j):
#     s[i][j] = 1
#     queue = [[i,j]]
#     while queue:
#         a,b = queue[0][0], queue[0][1]
#         del queue[0]
#         for k in range(4):
#             x = a + dx[k]
#             y = b + dy[k]
#             if 0 <= x < n and 0 <= y < m and s[x][y] == "1":
#                 queue.append([x,y])
#                 s[x][y] = s[a][b] + 1
#
# bfs(0,0)
# print(s[n-1][m-1])