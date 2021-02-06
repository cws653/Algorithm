import sys
input = sys.stdin.readline()
s = list(input.strip())
len_s = len(s)
d = [0 for i in range(len_s+1)]
d[0], d[1] = 1, 1
if s[0] == "0":
    print(0)
else:
    for i in range(2, len_s+1):
        if int(s[i-1]) > 0:
            d[i] += d[i-1]
        num = int(s[i-1]) + int(s[i-2])*10
        if 10 <= num <= 26:
            d[i] += d[i-2]
    print(d[len_s] % 1000000)