s = list(map(int, input().split()))
a = s[0]
b = s[1]
c = s[2]
print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)