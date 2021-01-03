# m, n = map(int, input().split())
# count = 0
# def finddecimal(x):
#     if x < 2:
#         return  False
#     for i in range(2, x):
#         if x%i == 0:
#             return False
#     return True
#
# for i in range(m, n+1):
#     if finddecimal(i):
#         print(i)

def isSoSu(x):
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            return False
    return 1*(x != 1)

a,b = map(int, input().split())

for i in range(int(a), int(b)+1):
    if isSoSu(i) == 1:
        print(i)