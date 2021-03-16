a,b = input().split()
b = int(b)

cnt,res = 0,0
for c in a[::-1]:
    result = int(c) if c.isdigit() else ord(c) - 55
    res += result*(b**cnt)
    cnt += 1
print(res)