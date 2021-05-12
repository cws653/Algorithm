import sys
inputValue = sys.stdin.readline().strip()
ans = 1
if inputValue:
    ans = 26 if inputValue[0] == "c" else 10
    for i in range(1, len(inputValue)):
        if inputValue[i] == 'c':
            if inputValue[i-1] == 'c':
                ans *= 25
            else:
                ans *= 26
        else:
            if inputValue[i-1] == 'd':
                ans *= 9
            else:
                ans *= 10

print(ans)
