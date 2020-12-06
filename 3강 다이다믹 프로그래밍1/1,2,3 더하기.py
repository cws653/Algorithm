# n의 값을 구하는 경우의 수
# n-1, n-2, n-3의 경우의 수 모두를 더한다.
# 이걸 소스로 표현하면?

t = int(input())

s = [1, 2, 4]
for i in range(3, 11):
    s.append(s[i-1] + s[i-2] + s[i-3])

for i in range(t):
    n = int(input())
    print(s[n - 1])