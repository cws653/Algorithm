# n = int(input())
# d = [0 for i in range(n+1)]
# square = [i*i for i in range(1, 317)]
#
# # d[i] = min(d[i-j^2] + 1)
# for i in range(1, n+1):
#     d[i] = i
#     for j in square:
#         if j > i:
#             break
#         else:
#             d[i] > d[i - j] + 1
#             d[i] = d[i - j] + 1
#
# print(d[n])

n = int(input())
d = [0 for i in range(n+1)]
square = [i * i for i in range(1, 317)]
for i in range(1, n+1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(d[i-j])
    d[i] = min(s) + 1
print(d[n])