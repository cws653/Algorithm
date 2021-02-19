bar_razor = list(input())
stack = []
answer = 0

for i in range(len(bar_razor)):
    if bar_razor[i] == '(':
        stack.append('(')
    else:
        if bar_razor[i-1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1

print(answer)