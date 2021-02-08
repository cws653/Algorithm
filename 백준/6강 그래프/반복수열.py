# import sys
# a,p = map(int, sys.stdin.readline().split())
# s = [a]
# visit = [0] * 25000
# visit[a] = 1
#
# while True:
#     t = s[-1]
#     val = 0
#     while t:
#         val += ((t%10)**p)
#         t //= 10
#     if visit[val] == 0:
#         s.append(val)
#         visit[val] = 1
#     else:
#         break
#
# sys.stdout.write(len(s[:s.index(val)]))

import sys
a,p = map(int, sys.stdin.readline().split())
s = [a]

while True:
    t = s[-1]
    val = 0
    while t:
        val += (t%10)**p
        t //= 10
    if val in s:
        print(len(s[:s.index(val)]))
        break
    else:
        s.append(val)

