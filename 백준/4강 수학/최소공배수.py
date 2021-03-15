t = int(input())

def GCD(x,y):
    if y == 0:
        return x
    else:
        return GCD(y,x%y)

def LCM(x,y):
    result = (x*y)//GCD(x,y)
    return result

def LCM2(x,y):
    if x>y:
        max = x
    else:
        max = y
    for i in range(max,(x*y)+1):
        if i%x == 0 and i%y == 0:
            res = i
            break
    return res

for _ in range(t):
    a,b = map(int, input().split())
    print(LCM(a,b))
