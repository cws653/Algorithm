t = int(input())
ott = [1,2,4]

for i in range(3, 10):
    ott.append(ott[i-1] + ott[i-2] + ott[i-3])

for _ in range(t):
    n = int(input())
    print(ott[n-1])