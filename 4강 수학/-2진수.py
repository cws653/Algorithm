a = int(input())
s = ''
if a == 0:
    print(0)
else:
    while a != 0:
        if a % 2:
            s += '1'
            a = a//-2 + 1
        else:
            s += '0'
            a //= -2
    print(s[::-1])