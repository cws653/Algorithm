input = int(input())

s = [[0 for i in range(10)] for j in range(101)]


for i in range(1, 10):
    s[1][i] = 1

for i in range(2,input + 1):
    for j in range(10):
        if j == 0:
            s[i][j] = s[i-1][1]
        elif j == 9:
            s[i][j] = s[i-1][8]
        else:
            s[i][j] = s[i-1][j-1] + s[i-1][j+1]

print(sum(s[input]) % 1000000000)






