# s = [True]*1000001
#
# def  findDecimal(x):
#     if x < 2:
#         return False
#     for i in range(2, int(x**0.5)+1):
#         if x%i == 0:
#             return False
#     return True
#
# for i in range(2, len(s)):
#     if findDecimal(i):
#         s[i] = True
#     else:
#         s[i] = False

# d = []
# def makeEratos(x):
#     if x == 0:
#         return False
#     s = [False, False] + [True] * x
#     for i in range(2, int(len(s)**0.5)+1):
#         if s[i] == True:
#             for j in range(i+i, len(s), i):
#                 s[j] = False
#     return s
# d = makeEratos(1000000)
#
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     A = 0
#     B = n
#     for i in range(10000000):
#         if d[A] and d[B]:
#             print(f"{n} = {A} + {B}")
#             break
#         A += 1
#         B -= 1
#     else:
#         print("Goldbach's conjection is wrong.")

Max = 1000000
s = [False, False] + [True] * Max
prime = []
for i in range(2, int(len(s)**0.5)+1):
    if s[i] == True:
        for j in range(i+i, len(s), i):
            s[j] = False
prime = [i for i in range(2, Max) if s[i] == True]

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(len(prime)):
        if s[n - prime[i]] == True:
            print(f"{n} = {prime[i]} + {n-prime[i]}")
            break