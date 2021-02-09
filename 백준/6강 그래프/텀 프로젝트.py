import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    global result
    visit[x] = 1
    cycle.append(x)
    y = s[x]
    if visit[y] == 1:
        if y in cycle:
            result += cycle[cycle.index(y):]
        return
    else:
        dfs(y)

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    s = [0] + list(map(int, sys.stdin.readline().split()))
    visit = [0 for i in range(n+1)]
    result = []

    for i in range(1, n+1):
        if visit[i] == 0:
            cycle = []
            dfs(i)

    print(n - len(result))