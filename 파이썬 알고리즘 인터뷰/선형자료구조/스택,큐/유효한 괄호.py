input_value = '()[]{}'
stack = []
check_value = {
    ')':'(',
    '}':'{',
    ']':'['
}

for i in input_value:
    if i not in check_value:
        stack.append(i)
    elif not stack or check_value[i] != stack.pop():
        print(False)

if len(stack) == 0:
    print(True)