t = int(input())

def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x%y)

for i in range(t):
    s = list(map(int, input().split()))
    sum = 0
    for j in range(1, s[0]+1):
        for k in range(j+1, s[0]+1):
            sum += GCD(s[j], s[k])
    print(sum)