# import sys
# n = int(sys.stdin.readline())
# s = []
# for i in range(n):
#     s.append(int(sys.stdin.readline()))
# s.sort()
# for i in range(n):
#     print(s[i])

# 문제: 위 알고리즘을 사용하면 충분히 배열정렬을 할 수 있으나 메모리 부족이라는 에러가 발생한다.
#      이에 메모리 부족문제를 해결할 수 있는 방안을 찾아본 결과 아래와 같은 방법을 사용해야한다는 것을 알았다.
#      그리고 왜 메모리 부족이라는 문제점이 생겼나 아래 알고리즘하고 비교해본 결과, sort() 함수가 메모리를 많이 잡아먹는 것이라고 판단되었다.

import sys
n = int(sys.stdin.readline())
s = [0] * 10001

for i in range(n):
    a = int(sys.stdin.readline())
    s[a] += 1

for i in range(10001):
    if s[i] != 0:
        for j in range(s[i]):
            print(i)