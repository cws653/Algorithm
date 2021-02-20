from collections import deque
import sys
n = int(sys.stdin.readline())
q = deque()
for _ in range(n):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        q.append(s[1])
    elif s[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            x = q.popleft()
            print(x)
    elif s[0] == 'size':
        print(len(q))
    elif s[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if q:
            print(q[len(q)-1])
        else:
            print(-1)
