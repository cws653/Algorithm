value = 'bcabc'

# 내가 푼 답
# stack = []
#
# for i in value:
#     if i not in stack:
#         stack.append(i)
#     else:
#         continue
# stack.sort()
# print(''.join(stack))

# 정답
import collections
counter, seen, stack = collections.Counter(value), set(), []

for i in value:
    counter[i] -= 1
    if i in seen:
        continue
    # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
    while stack and i < stack[-1] and counter[stack[-1]] > 0:
        seen.remove(stack.pop())
    stack.append(i)
    seen.add(i)
print(''.join(stack))
