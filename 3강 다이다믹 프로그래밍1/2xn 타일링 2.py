# d[n] = d[n-1] + 2*d[n-2]

n = int(input())
d = [0 for i in range(n+1)]
d[0] = 1
d[1] = 1
for i in range(2, n+1):
    d[i] = d[i-1] + 2*d[i-2]

print(d[n] % 10007)
