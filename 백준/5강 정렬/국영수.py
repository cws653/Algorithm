import sys
n = int(sys.stdin.readline())
s = []
for i in range(n):
    # a = list(sys.stdin.readline().split())
    # s.append(a)
    a,b,c,d = sys.stdin.readline().split()
    s.append([a,int(b),int(c),int(d)])

s.sort(key=lambda x: (-x[1],x[2],-x[3],x[0]))

for i in range(n):
    print(s[i][0])