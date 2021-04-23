import sys
n = int(sys.stdin.readline())
q = []
for _ in range(n):
    s = list(sys.stdin.readline().split())

    if s[0] == 'push':
        q.insert(0, s[1])
    elif s[0] == 'pop':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(q))
    elif s[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        if q:
            print(q[len(q) - 1])
        else:
            print(-1)
    elif s[0] == 'back':
        if q:
            print(q[0])
        else:
            print(-1)