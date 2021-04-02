height = [0,1,0,2,1,0,1,3,2,1,2,1]

# 첫번째 해결방안
if not height:
    print(0)

volume = 0
left, right = 0, len(height) - 1
left_max, right_max = height[left], height[right]

while left < right:
    left_max = max(height[left], left_max)
    right_max = max(height[right], right_max)
    if left_max <= right_max:
        volume += left_max - height[left]
        left += 1
    else:
        volume += right_max - height[right]
        right -= 1

print(volume)


# # 두번째 해결방안
# stack = []
# volume = 0
# for i in range(len(height)):
#     print(stack)
#     while stack and height[i] > height[stack[-1]]:
#         top = stack.pop()
#
#         if not len(stack):
#             break
#
#         distance = i - stack[-1] - 1
#         waters = min(height[i], height[stack[-1]]) - height[top]
#
#         volume += distance * waters
#
#     stack.append(i)
# print(volume)