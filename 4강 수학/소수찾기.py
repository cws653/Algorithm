n = int(input())
s = list(map(int, input().split()))
count = 0
def findecimal(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

for i in s:
    if findecimal(i):
        count += 1
print(count)

