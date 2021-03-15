a,b = map(int, input().split())

def GCD(x,y):
    if y == 0:
        return x
    else:
        return GCD(y,x%y)

def LCM(x,y):
    result = (x*y) // GCD(x,y)
    return result

print(GCD(a,b))
print(LCM(a,b))