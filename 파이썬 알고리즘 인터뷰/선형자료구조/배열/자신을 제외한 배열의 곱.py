nums = [1,2,3,4]

# 첫번째 풀이방법
# sum = 1
# result = []
# for i in range(len(nums)):
#     sum = 1
#     for j in range(len(nums)):
#        if j == i:
#            continue
#        else:
#            sum *= nums[j]
#     result.append(sum)
#
# print(result)

# 두번째 풀이방법
out = []
p = 1
for i in range(len(nums)):
    out.append(p)
    p = p * nums[i]

p = 1
for i in range(len(nums)-1, -1, -1):
     out[i] = out[i] * p
     p = p * nums[i]

print(out)
