n,k = map(int, input().split())
s = [i for i in range(1,n+1)]
stack = []
index = 0
for _ in range(n):
    index += k-1
    if index >= len(s):
        index = index%len(s)
    stack.append(str(s.pop(index)))

print("<",", ".join(stack),">", sep='')