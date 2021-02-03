import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    s = [0] + list(map(int, sys.stdin.readline().split()))
    visit = [0]*(n+1)

    group = 1
    for i in range(1,n+1):
        if visit[i] == 0:
            while visit[i] == 0:
                visit[i] = group
                i = s[i]
            while visit[i] == group:
                visit[i] = -1
                i = s[i]
            group += 1

    cnt = 0
    for v in visit:
        if v > 0:
            cnt += 1

    sys.stdout.write("{}\n".format(cnt))