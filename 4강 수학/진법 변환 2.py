a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, d = map(int, input().split())
ans = ""

while n != 0:
    ans += a[n % d]
    n //= d

print(ans[::-1])