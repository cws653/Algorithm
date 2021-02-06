import sys
n = int(sys.stdin.readline())
s = []
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    s.append([a,b])

s.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    print(s[i][0], s[i][1])