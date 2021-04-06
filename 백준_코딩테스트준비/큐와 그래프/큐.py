import sys
inputInt = int(sys.stdin.readline())
q = []
for _ in range(inputInt):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        q.insert(0, s[1])

    elif s[0] == 'pop':
        if len(q) > 0:
            print(q.pop())
        else:
            print(-1)

    elif s[0] == 'size':
        print(len(q))

    elif s[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)

    elif s[0] == 'front':
        if len(q) > 0:
            print(q[len(q) - 1])
        else:
            print(-1)

    elif s[0] == 'back':
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)