n = int(input())
s = list(map(int, input().split()))

def decimal(x):
    if x < 2:
        return False
    else:
        for i in range(2, int((x**0.5)+1)):
            if x%i == 0:
                return False
        return True

sum = 0
for i in s:
    if decimal(i):
        sum += 1

print(sum)