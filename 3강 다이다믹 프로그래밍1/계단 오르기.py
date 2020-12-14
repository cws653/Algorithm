# n = int(input())
# a = [0 for i in range(301)]
# d = [[0 for i in range(n+1)] for j in range(301)]
# for i in range(n):
#     a.append(int(input()))
# d[0][1] = a[0]
# for i in range(2, n+1):
#     d[1][i] = d[0][i-1] + a[i-1]
#     d[0][i] = max(d[0][i-2], d[1][i-2]) + a[i-1]
# print(max(max(d[0], d[1])))

n = int(input())
a = [0 for i in range(301)]
d = [0 for i in range(301)]
for i in range(n):
    a.append(int(input()))
d[0] = a[0]
d[1] = a[1] + a[0]
d[2] = max(a[2] + a[1], a[2] + a[0])
for i in range(3, n):
    d[i] = max(d[i-3] + a[i-1] + a[i], d[i-2] + a[i])
print(d[n-1])