num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a,b = map(int, input().split())
ans = ''

while a != 0:
    ans += num[a%b]
    a //= b

print(ans[::-1])