m,n = map(int, input().split())

def decimal(x):
    if x < 2:
        return False
    else:
        for i in range(2,int((x**0.5)+1)):
            if x%i == 0:
                return False
        return True

for i in range(m,n+1):
    if decimal(i):
        print(i)