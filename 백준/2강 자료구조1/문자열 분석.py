
# while True:
#     try:
#         input = input()
#         print(input)
#     except:
#         break
#
#     answear = [0] * 4
#     for i in input:
#         if 65 <= ord(i) <= 90:
#             answear[0] += 1
#         elif 97 <= ord(i) <= 122:
#             answear[1] += 1
#         elif 48 <= ord(i) <= 57:
#             answear[2] += 1
#         elif i == " ":
#             answear[3] += 1
#
#     # for i in answear:
#     #     print(i, end=" ")
#     print(*answear)

import sys

while True:
    line = sys.stdin.readline().rstrip('\n')
    print(line)
    up, lo, sp, nu = 0, 0, 0, 0

    if not line:
        break
    for i in line:
        if i.isupper():
            up += 1
        elif i.islower():
            lo += 1
        elif i.isdigit():
            nu += 1
        elif i.isspace():
            sp += 1

    sys.stdout.write("{} {} {} {}\n".format(lo, up, nu, sp))
# import sys
#
# while True:
#     line = sys.stdin.readline().rstrip('\n')
#     print(line)
    # if not line:
    #     break
    # for i in line:
    #    print(i)