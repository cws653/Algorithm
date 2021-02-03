import sys
n = int(sys.stdin.readline())
matrix = [[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]

for i in range(n):
    line = sys.stdin.readline().strip()
    for j, a in enumerate(line):
        matrix[i][j] = int(a)

# 좌,우,상,하
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(x, y, c):
    visited[x][y] = 1
    global num
    if matrix[x][y] == 1:
        num += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                dfs(nx, ny, c)

cnt = 1
numlist = []
num = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and visited[i][j] == 0:
            dfs(i,j,cnt)
            numlist.append(num)
            num = 0

print(len(numlist))
for n in sorted(numlist):
    print(n)
