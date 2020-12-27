t = int(input())
def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x % y)

for _ in range(t):
    s = list(map(int, input().split()))
    n = s.pop(0)
    sum = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sum += GCD(s[i], s[j])
    print(sum)