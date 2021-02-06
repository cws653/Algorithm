N, M = map(int, input().split())

originalList = []
answer = []
popNum = 0

for i in range(N):
    originalList.append(i+1)

print(originalList)

for i in range(N):
    print(originalList)
    popNum += M-1
    print(popNum)
    if popNum > len(originalList):
        popNum = popNum % len(originalList)
    popElement = originalList.pop(popNum)
    answer.append(popElement)

print(answer)
# 문제를 풀 때 머리로 원을 그리고 숫자에 맞게 돌려보는 상상하면 이해가 잘 간다.