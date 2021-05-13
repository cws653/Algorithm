n = int(input())
B = list(map(int, input().split()))

def go(x, b, A):
    b.remove(x)
    A.append(x)
    least_one = False
    if not b:
        return True
    if x * 2 in b:
        least_one = True
        return go(x * 2, b, A)
    if x % 3 == 0 and x // 3 in b:
        least_one = True
        return go(x // 3, b, A)
    if not least_one:
        return False

for i in range(n):
    A = []
    flag = go(B[i], B.copy(), A)
    if flag:
        print(*A)
        break