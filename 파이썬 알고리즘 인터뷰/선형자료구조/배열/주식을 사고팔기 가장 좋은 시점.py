nums = [7,1,5,3,6,4]

# 첫번쨰 풀이
max_price = 0

for i, price in enumerate(nums):
    for j in range(i, len(nums)):
        max_price = max(nums[j] - price, max_price)

print(max_price)

# 두번째 풀이
import sys
profit = 0
min_price = sys.maxsize

for price in nums:
    min_price = min(min_price, price)
    profit = max(profit, price - min_price)

print(profit)