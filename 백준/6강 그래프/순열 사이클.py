import sys
sys.setrecursionlimit(2000)

def dfs(x):
    visit[x] = 1
    number = numbers[x]
    if visit[number] == 0:
        dfs(number)


for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    visit = [0 for i in range(n+1)]
    numbers = [0] + list(map(int, sys.stdin.readline().split()))
    result = 0
    for i in range(1, n+1):
        if visit[i] == 0:
            dfs(i)
            result += 1
    print(result)