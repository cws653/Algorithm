enable = {str(i) for i in range(10)}

N = int(input())
M = int(input())
if M != 0:
    enable -= set(map(str, input().split()))

min_value = abs(100 - N)

for num in range(1000001):
    num = str(num)
    for i in range(len(num)):
        if num[i] not in enable:
            break
        elif i == len(num) - 1:
            min_value = min(min_value, abs(N - int(num)) + len(str(num)))

print(min_value)