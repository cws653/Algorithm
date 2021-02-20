import sys
s = list(sys.stdin.readline().rstrip())
stack = [-1 for i in range(26)]
for i in range(len(s)):
    if stack[ord(s[i])-97] != -1:
        continue
    else:
        stack[ord(s[i])-97] = i
for i in stack:
    print(i, end=' ')