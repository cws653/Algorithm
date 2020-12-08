a = int(input())
s = [[0 for i in range(10)] for j in range(1001)]

# print(len(s))

for i in range(10):
    s[1][i] = 1

for i in range(2, a+1):
    for j in range(10):
        for k in range(0, j+1):
            s[i][j] += s[i-1][k]

print(sum(s[a]) % 10007)