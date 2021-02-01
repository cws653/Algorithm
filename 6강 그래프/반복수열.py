import sys
a,p = map(int, sys.stdin.readline().split())
seq = [a]
while True:
    t = seq[-1]
    val = 0
    while t:
        val += ((t%10)**p)
        t //= 10

    if val in seq:
        sys.stdout.write(str(seq.index(val)))
        break
    else:
        seq.append(val)