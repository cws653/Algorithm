import sys

while True:
    stack = [0] * 4
    x = sys.stdin.readline().rstrip('\n')

    if not x:
        break
    for i in x:
        if 97 <= ord(i) <= 122:
            stack[0] += 1
        elif 65 <= ord(i) <= 90:
            stack[1] += 1
        elif 48 <= ord(i) <= 57:
            stack[2] += 1
        elif i == ' ':
            stack[3] += 1

    for i in stack:
        print(i, end= ' ')
    print()