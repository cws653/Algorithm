# 이 방법을 사용하면 런타임 에러가 발생한다.
# 그 이유는 d 배열 값을 구할 때 for문을 계속해서 돌다보니 시간복잡도가 올라가기 때문이다.
# t = int(input())
#
# for i in range(t):
#     n = int(input())
#     # d[n] = d[n-1] + d[n-5]
#     d = [0 for i in range(n+1)]
#     d[1] = d[2] = d[3] = 1
#     d[4] = d[5] = 2
#     for j in range(6, n+1):
#         d[j] = d[j-1] + d[j-5]
#     print(d[n])

# 이 방법을 사용하면 위의 문제를 해결할 수 있다.
t = int(input())
d = [0 for i in range(101)]
d[1] = d[2] = d[3] = 1
d[4] = d[5] = 2

for i in range(6, 101):
    d[i] = d[i-1] + d[i-5]

for i in range(t):
    n = int(input())
    print(d[n])

# 다른 방식은 변의 길이를 다른 점화식을 통해 구해서 푸는 것이다.
# 도형문제를 응용하면 다음과 같은 점화식이 추가로 나오게 된다.
# d[n] = d[i-2] + d[i-3]
# 위 점화식을 사용하면 다른 코드를 통해서 문제를 해결할 수 있다.



