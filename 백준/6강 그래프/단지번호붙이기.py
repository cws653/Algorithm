# import sys
# from collections import deque
#
# n = int(sys.stdin.readline())
# s = []
# visit = [[0 for i in range(n)] for i in range(n)]
#
# # 상하좌우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 0]
# cnt = []
# def bfs(x,y):
#     visit[x][y] = 1
#     q = deque()
#     q.append([x,y])
#     count = 1
#     while q:
#         a,b = q.popleft()
#         for i in range(4):
#             nx = a + dx[i]
#             ny = b + dy[i]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if visit[nx][ny] == 0 and s[nx][ny] == 1:
#                     visit[nx][ny] = 1
#                     q.append([nx,ny])
#                     count += 1
#     cnt.append(count)
#
# for _ in range(n):
#     s.append(list(map(int, sys.stdin.readline().strip())))
#
# for i in range(n):
#     for j in range(n):
#         if visit[i][j] == 0 and s[i][j] == 1:
#             bfs(i,j)
#
# cnt.sort()
# print(len(cnt))
# for i in cnt:
#     print(i)

import sys
from collections import deque

n = int(input())
s = []
cnt = []

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    s[x][y] = 0
    q = deque()
    q.append([x,y])
    count = 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny <n and s[nx][ny] == 1:
                s[nx][ny] = 0
                q.append([nx, ny])
                count += 1
    cnt.append(count)

for _ in range(n):
    s.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if s[i][j] == 1:
            bfs(i,j)

cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)