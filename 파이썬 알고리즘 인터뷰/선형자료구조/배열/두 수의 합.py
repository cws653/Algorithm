# # 해결방안 1 (내가 처음에 푼 방법)
# nums = [2,7,11,15]
# a,b = 0,0
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == 9:
#             a = i
#             b = j
# ans = [a,b]
# print(ans)

# 해결방안 2
nums = [2,7,11,15]
a,b = 0,0
for i,num in enumerate(nums):
    completion = 9 - num

    if completion in nums[i+1:]:
        a = nums.index(num)
        b = nums[i+1:].index(completion) + (i+1)

print(a,b)