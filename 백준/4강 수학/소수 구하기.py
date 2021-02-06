# def getPrimaryNum_Eratos(N):
#     nums = [True] * N
#     for i in range(2, int(len(nums)**0.5+1)):
#         if nums[i] == True:
#             for j in range(i+i, N, i):
#                 nums[j] = False
#     return [i for i in range(2, N) if nums[i] == True]

def findDecimal(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5+1)):
        if x % i == 0:
            return False
    return True


m,n = map(int, input().split())

for i in range(m, n+1):
    if findDecimal(i):
        print(i)