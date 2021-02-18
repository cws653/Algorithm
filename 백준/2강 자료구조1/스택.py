import sys
n = int(sys.stdin.readline())
s = []
for _ in range(n):
    a = sys.stdin.readline().split()
    if "push" in a:
      b = int(a[1])
      s.append(b)
    elif "pop" in a:
        if len(s) > 0:
            print(s.pop())
        else:
            print(-1)
    elif "size" in a:
        print(len(s))
    elif "empty" in a:
        if len(s) == 0:
            print(1)
        else:
            print(0)
    elif "top" in a:
        if len(s) > 0:
            print(s[len(s) - 1])
        else:
            print(-1)