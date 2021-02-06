import sys
n = int(sys.stdin.readline())
nums = []
for i in range(n):
    num = int(sys.stdin.readline())
    nums.append((num, i))

nums_sorted = sorted(nums, key=lambda x: x[0])

ans = 0

for i in range(n):
    ans = max(nums_sorted[i][1] - i + 1, ans)

print(ans)

# 결과 : 기존 index값 - 소팅한 index