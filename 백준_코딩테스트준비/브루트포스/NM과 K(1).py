n,m,k = map(int, input().split())
num_list = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ans = -1000000

def go(px, py, index, sum):
    if index == k:
        global ans

        if ans < sum:
            ans = sum
        return

    for x in range(px, n):
        for y in range(py if x == px else 0, m):
            if visited[x][y]:
                continue

            ok = True

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny]:
                        ok = False

            if ok:
                visited[x][y] = True
                go(x, y, index+1, sum+num_list[x][y])
                visited[x][y] = False

go(0,0,0,0)
print(ans)