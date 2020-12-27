t = int(input())

def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x%y)

for i in range(t):
    a, b = map(int, input().split())
    g = GCD(a, b)
    print(a*b//g)