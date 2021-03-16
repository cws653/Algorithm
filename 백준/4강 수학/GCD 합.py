t = int(input())

def GCD(x,y):
    if y == 0:
        return x
    else:
        return GCD(y, x%y)

for _ in range(t):
    sum = 0
    s = list(map(int, input().split()))
    d = s[1:]
    for i in range(len(d)):
        for j in range(i+1,len(d)):
            sum += GCD(d[i],d[j])
    print(sum)