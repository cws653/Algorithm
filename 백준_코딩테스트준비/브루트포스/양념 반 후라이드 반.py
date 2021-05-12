import sys
a,b,c,x,y = map(int, sys.stdin.readline().split())
if a+b<c*2:
    print(a*x+b*y)
else:
    m = min(x,y)
    print(c*m*2+min(c*2,a)*max(0,x-m)+min(c*2,b)*max(0,y-m))