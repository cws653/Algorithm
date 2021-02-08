# import sys
# from collections import deque
#
# t = int(sys.stdin.readline())
#
# def bfs(x):
#     visit[x] = 1
#     q = deque()
#     q.append(x)
#     while q:
#         a = q.popleft()
#         for b in range(1, v+1):
#             if s[a][b] == 1 and visit[b] == 0:
#                 visit[b] = -visit[a]
#                 q.append(b)
#             else:
#                 if s[a][b] == 1 and visit[a] == visit[b]:
#                     return False
#     return True
#
# for _ in range(t):
#     v,e = map(int, sys.stdin.readline().split())
#     s = [[0 for _ in range(v+1)] for _ in range(v+1)]
#     visit = [0 for _ in range(v+1)]
#     isTrue = True
#     for _ in range(e):
#         a,b = map(int, sys.stdin.readline().split())
#         s[a][b] = 1
#         s[b][a] = 1
#     for i in range(1, v+1):
#         if visit[i] == 0:
#             if not bfs(i):
#                 isTrue = False
#                 break
#
#     print("Yes" if isTrue else "No")

import sys
from collections import deque
t = int(sys.stdin.readline())

def bfs(x):
    visit[x] = 1
    q = deque()
    q.append(x)
    while q:
        a = q.popleft()
        for i in s[a]:
            if visit[i] == 0:
                visit[i] = -visit[a]
                q.append(i)
            else:
                if visit[i] == visit[a]:
                    return False
    return True

for _ in range(t):
    v,e = map(int, sys.stdin.readline().split())
    visit = [0 for i in range(v + 1)]
    s = [[] for i in range(v+1)]
    isTrue = True
    for _ in range(e):
        a,b = map(int, sys.stdin.readline().split())
        s[a].append(b)
        s[b].append(a)
    for i in range(1, v+1):
        if visit[i] == 0:
            if not bfs(i):
                isTrue = False

    print("YES" if isTrue else "NO")
