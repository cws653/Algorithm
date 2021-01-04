a,b = map(int, input().split())

def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x%y)

print(GCD(a, b))
print((a*b)//GCD(a,b))