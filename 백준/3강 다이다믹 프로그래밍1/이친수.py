n = int(input())

d = [0,1,1]
for i in range(3,91):
    d.append(d[i-2] + d[i-1])
print(d[n])
