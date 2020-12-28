# import sys
# before, base = sys.stdin.readline().split()
# base = int(base)
#
# cnt, res = 0, 0
# for c in before[::-1]:
#     target = int(c) if c.isdigit() else ord(c) - 55
#     res += (target * (base**cnt))
#     cnt += 1
#
# sys.stdout.write(str(res))

dic_a = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
n, d = map(str, input().split())
d = int(d)

result = 0
for i, b in enumerate(n[::-1]):
    result = result + dic_a[b] * (d**i)

print(result)