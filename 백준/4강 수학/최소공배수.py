t = int(input())

def GCD(x,y):
    if y == 0:
        return x
    else:
        return GCD(y,x%y)

def LCM(x,y):
    return (x*y)//GCD(x,y)

for i in range(t):
    a,b = map(int, input().split())
    print(LCM(a,b))