nums = [1,4,3,2]

# 첫번째 문제풀이
pair = []
sum = 0
nums.sort()

for i in nums:
    pair.append(i)
    if len(pair) == 2:
        sum += min(pair)
        pair = []
print(sum)