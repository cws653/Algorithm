import sys
a = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline())
stack_right = []
stack_left = []
stack = []

for i in range(len(a)):
    stack_left.append(a[i])

for i in range(n):
    b = list(sys.stdin.readline().split())
    if b[0] == 'L':
        if stack_left:
            x = stack_left.pop()
            stack_right.append(x)
    elif b[0] == 'D':
        if stack_right:
            x = stack_right.pop()
            stack_left.append(x)
    elif b[0] == 'B':
        if stack_left:
            stack_left.pop()
    elif b[0] == 'P':
        stack_left.append(b[1])

stack = stack_left + list(reversed(stack_right))
str_stack = ''.join(stack)
print(str_stack)