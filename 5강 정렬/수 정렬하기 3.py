# import sys
# n = int(sys.stdin.readline())
# s = [int(sys.stdin.readline()) for _ in range(n)]
# s.sort()
# for i in range(n):
#     print(s[i])

import sys
n = int(sys.stdin.readline())
s = [0] * 10001
for i in range(n):
    s[int(sys.stdin.readline())] += 1
for i in range(10001):
    if s[i] != 0:
        for j in range(s[i]):
            print(i)