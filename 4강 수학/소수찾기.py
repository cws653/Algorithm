n = int(input())

def findDecimal(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5+1)):
        if x % i == 0:
            return False
    return True

s = list(map(int, input().split()))
sum = 0
for i in range(len(s)):
    if findDecimal(s[i]):
        sum += 1

print(sum)