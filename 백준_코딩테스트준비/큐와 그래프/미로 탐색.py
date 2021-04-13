import sys
n,m = map(int, sys.stdin.readline().split())
s = []
for _ in range(n):
    s.append(list(sys.stdin.readline().strip()))

dx = [1,-1,0,0]
dy = [0,0,-1,1]

queue = [[0,0]]
s[0][0] = 1
while queue:
    a,b = queue[0][0],queue[0][1]
    del queue[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m:
            if s[x][y] == "1":
                queue.append([x,y])
                s[x][y] = s[a][b] + 1

print(s[n-1][m-1])