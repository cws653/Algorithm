s = input()
n = len(s)
answer = ''
ans = 0
count = 0
for i in range(n-1, -1, -1):
    if count % 3 == 0:
        ans += int(s[i]) * 1
        count += 1
    elif count % 3 == 1:
        ans += int(s[i]) * 2
        count += 1
    elif count % 3 == 2:
        ans += int(s[i]) * 4
        answer += str(ans)
        ans = 0
        count = 0
if ans >= 0:
    answer += str(ans)
answer = answer[::-1]
print(int(answer))