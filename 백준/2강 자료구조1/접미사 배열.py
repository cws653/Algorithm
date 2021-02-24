# import sys
# s = list(sys.stdin.readline().rstrip())
# stack = []
# stack.append(''.join(s))
# for i in range(len(s)-1):
#     del s[0]
#     stack.append(''.join(s))
#
# stack.sort()
#
# for a in stack:
#     print(a)

S = str(input())
S_list = []

for _ in S:
    S_list.append(S)
    S = S[1:]

for i in sorted(S_list):
    print(i)