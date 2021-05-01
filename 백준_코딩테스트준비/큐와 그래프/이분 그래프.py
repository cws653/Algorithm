import sys
from collections import deque
t = int(sys.stdin.readline())

def bfs(x):
    bi[x] = 1
    q = deque()
    q.append(x)
    while q:
        a = q.popleft()
        for i in s[a]:
            if bi[i] == 0:
                bi[i] = -bi[a]
                q.append(i)
            else:
                if bi[i] == bi[a]:
                    return False
    return True

for _ in range(t):
    v,e = map(int, sys.stdin.readline().split())
    s = [[] for i in range(v+1)]
    bi = [0 for i in range(v+1)]
    isTrue = True
    for i in range(e):
        a,b = map(int, sys.stdin.readline().split())
        s[a].append(b)
        s[b].append(a)
    for j in range(1,v+1):
        if bi[j] == 0:
            if not bfs(j):
                isTrue = False
                break
    print("YES" if isTrue else "NO")