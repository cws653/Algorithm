# a = input()
# a = a[::-1]
# sum = 0
#
# for i in range(len(a)):
#     sum += int(a[i])*(2**i)
#
# eight = ''
# while sum > 0:
#     eight += str(sum%8)
#     sum //= 8
#
# print(eight[::-1])

print(oct(int(input(), 2))[2:])