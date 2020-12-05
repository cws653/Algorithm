# input = int(input())
#
# rootNum = 0
# while input > 1:
#     if input % 3 == 0:
#         rootNum += 1
#         input = input / 3
#     elif input % 2 == 0:
#         input = input / 2
#         rootNum += 1
#     else:
#         input = input - 1
#         rootNum += 1

# print(rootNum)

a = int(input())
minimum = [a]
count = 0
def cal(a):
    list = []
    for i in a:
        list.append(i-1)
        if i%3 == 0:
            list.append(i/3)
        if i%2 == 0:
            list.append(i/2)
    return  list

while True:
    if a == 1:
        print(a)
        break
    temp = minimum[:]
    minimum = []
    minimum = cal(temp)
    count += 1
    if min(minimum) == 1:
        print(count)
        break