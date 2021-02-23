import sys
s = list(sys.stdin.readline().rstrip())
stack = [0] * 26
for i in s:
    x = ord(i) - 97
    stack[x] = stack[x] + 1

for i in stack:
    print(i, end= ' ')