a,b = map(int, input().split())
s = '0123456789ABCDEFGHIJKLMLOPQRSTUVWXYZ'
ans = ''

while a != 0:
    ans += s[a%b]
    a //= b

print(ans[::-1])