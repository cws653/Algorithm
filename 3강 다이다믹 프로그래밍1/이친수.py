# D[n] = D[n-1] + D[n-2]

s = [0,1,1]

for i in range(3, 91):
    s.append(s[i - 2] + s[i - 1])
n = int(input())
print(s[n])