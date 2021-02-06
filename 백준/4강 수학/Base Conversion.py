a,b = map(int, input().split())
m = int(input())
s = list(map(int, input().split()))

def toTen(x, a):
    sum = 0
    x = x[::-1]
    for i in range(len(x)):
        sum += x[i] * (a**i)
    return sum

def toOther(x, a):
    d = []
    while x:
        d.append(str(x%a))
        x //= a
    return d[::-1]

print(' '.join(toOther(toTen(s,a),b)))

