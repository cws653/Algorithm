import sys
from collections import deque

def bfs(x,y,s):
    days = -1

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while mydeque:
        days += 1
        for _ in range(len(mydeque)):
            a,b = mydeque.popleft()

            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < n and 0 <= ny < m and s[nx][ny] == 0:
                    s[nx][ny] = s[a][b] + 1
                    mydeque.append([nx,ny])

    for i in s:
        if 0 in i:
          return -1
    return days

m,n = map(int, sys.stdin.readline().split())
s = []
mydeque = deque()
for i in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            mydeque.append([i,j])

print(bfs(m,n,s))

