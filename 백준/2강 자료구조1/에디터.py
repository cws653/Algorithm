

# # 소스 1번
# inputString = input().strip()
# inputInt = int(input())
# position = len(inputString) + 1
# print(position)
#
# for i in range(inputInt):
#     inputDetail = input()
#     # print(inputDetail)
#     if "P" in inputDetail:
#         # print(inputString[0:position - 1])
#         # print(inputString[position - 1:])
#         inputString = inputString[0:position - 1] + inputDetail[2] + inputString[position - 1:]
#         position += 1
#     elif "L" in inputDetail:
#         if position == 1:
#             position = position
#         else:
#             position -= 1
#     elif "D" in inputDetail:
#         if position == position + 1:
#             position = position
#         else:
#             position += 1
#     elif "B" in inputDetail:
#         if position == 1:
#             position == position
#         else:
#             inputString = inputString[0:position - 2] + inputString[position - 1:]
#             position -= 1
#     print(position)
#     print(inputString)print
#
#
#
# # 소스 2번

import sys
leftStack = list(sys.stdin.readline()[:-1])
# print(leftStack)
rightStack = list()
# print(rightStack)
testCase = int(sys.stdin.readline())
# print(testCase)

for _ in range(testCase):
    cmd = sys.stdin.readline()
    if cmd[0] == 'L' and leftStack:
        rightStack.append(leftStack.pop())
    elif cmd[0] == 'D' and rightStack:
        leftStack.append(rightStack.pop())
    elif cmd[0] == 'B' and leftStack:
        leftStack.pop()
    elif cmd[0] == 'P':
        leftStack.append(cmd[2])

# print(rightStack)
# print(rightStack[:-1])
# print(rightStack[::])
# print(rightStack[::-1])
sys.stdout.write(''.join(leftStack + rightStack[::-1]))