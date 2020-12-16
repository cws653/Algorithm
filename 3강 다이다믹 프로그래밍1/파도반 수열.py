p = [0 for i in range(101)]
s = [0,1,1,1,2,2,3,4,5,7,9]

for i in range(11):
    p[i] = s[i]

for i in range(10, 101):
    p[i] = p[i-1] + p[i-5]

t = int(input())
for i in range(t):
    n = int(input())
    print(p[n])