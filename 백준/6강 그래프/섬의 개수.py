# import sys
# from collections import deque
#
# dx = [-1,-1,-1,0,1,1,1,0]
# dy = [-1,0,1,1,1,0,-1,-1]
#
# def bfs(x,y):
#     visit[x][y] = 1
#     q = deque()
#     q.append([x,y])
#     while q:
#         a,b = q.popleft()
#         for i in range(8):
#             nx = a + dx[i]
#             ny = b + dy[i]
#             if 0 <= nx < h and 0 <= ny < w and visit[nx][ny] == 0 and s[nx][ny] == 1:
#                 visit[nx][ny] == 1
#                 q.append([nx, ny])
#
# while True:
#     w,h = map(int, sys.stdin.readline().split())
#     s = []
#     visit = [[0 for i in range(w)] for i in range(h)]
#     cnt = 0
#     if w == 0 and h == 0:
#         break
#
#     for i in range(h):
#         s.append(list(map(int, sys.stdin.readline().split())))
#
#     for i in range(h):
#         for j in range(w):
#             if visit[i][j] == 0 and s[i][j] == 1:
#                 bfs(i,j)
#                 cnt += 1
#     print(cnt)

import sys
from collections import deque

dx = [-1,-1,-1,0,1,1,1,0]
dy = [-1,0,1,1,1,0,-1,-1]

def bfs(x,y):
    s[x][y] = 0
    q = deque()
    q.append([x,y])
    while q:
        a,b = q.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == 1:
                s[nx][ny] = 0
                q.append([nx, ny])

while True:
    w,h = map(int, sys.stdin.readline().split())
    s = []
    cnt = 0
    if w == 0 and h == 0:
        break

    for i in range(h):
        s.append(list(map(int, sys.stdin.readline().split())))

    for i in range(h):
        for j in range(w):
            if s[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)
