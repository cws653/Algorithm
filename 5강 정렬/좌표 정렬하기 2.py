n = int(input())
s = []
for i in range(n):
    a,b = map(int, input().split())
    s.append([a,b])

s.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    print(s[i][0], s[i][1])