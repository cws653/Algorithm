import sys
from collections import deque

k = int(sys.stdin.readline())

def bfs(start):
    visit[start] = 1
    q = deque()
    q.append(start)
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

for i in range(k):
    v,e = map(int, sys.stdin.readline().split())
    s = [[] for i in range(v+1)]
    visit = [0 for i in range(v+1)]
    isTrue = True
    for j in range(e):
        a,b = map(int, sys.stdin.readline().split())
        s[a].append(b)
        s[b].append(a)
    for k in range(1, v+1):
        if visit[k] == 0:
            if not bfs(k):
                isTrue = False
                break
    print("YES"if isTrue else "NO")