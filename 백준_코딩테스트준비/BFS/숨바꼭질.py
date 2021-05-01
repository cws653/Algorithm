import sys
from collections import deque
n,k = map(int, sys.stdin.readline().split())
visit = [0 for i in range(100001)]
q = deque()
q.append([n,0])
while q:
    a,b = q.popleft()
    if visit[a] != 1:
        visit[a] = 1
        if a == k:
            break
        if 0 <= a+1 <= 100000 and visit[a+1] == 0:
            q.append([a+1, b+1])
        if 0 <= a-1 <= 100000 and visit[a-1] == 0:
            q.append([a-1, b+1])
        if 0 <= a*2 <= 100000 and visit[a*2] == 0:
            q.append([a*2, b+1])
print(q[0][1])