import sys
from collections import deque
s = int(sys.stdin.readline())
matrix = [[-1]*(s+1) for i in range(s+1)]

def bfs():
    q = deque([[1,0]])
    matrix[1][0] = 0
    while q:
        a,b = q.popleft()

        if matrix[a][a] == -1:
            matrix[a][a] = matrix[a][b] + 1
            q.append([a,a])
        if a+b <= s and matrix[a+b][b] == -1:
            matrix[a+b][b] = matrix[a][b] + 1
            q.append([a+b,b])
        if a-1 <= s and matrix[a-1][b] == -1:
            matrix[a-1][b] = matrix[a][b] + 1
            q.append([a-1,b])

bfs()

r = matrix[s][1]
for i in range(1, s):
    if matrix[s][i] != -1:
        r = min(r, matrix[s][i])
print(r)