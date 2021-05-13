N = int(input())
s = []
res = 0
for _ in range(N):
    s.append(list(map(str, input().strip())))

def check(s):
    cnt = 0
    for i in range(N):
        cnt_row = 1
        cnt_col = 1
        for j in range(N-1):
            if s[i][j] == s[i][j+1]:
                cnt_row += 1
            else:
                cnt = max(cnt, cnt_row)
                cnt_row = 1

            if s[j][i] == s[j+1][i]:
                cnt_col += 1
            else:
                cnt = max(cnt, cnt_col)
                cnt_col = 1
        cnt = max(cnt, cnt_row, cnt_col)
    return cnt

for i in range(N):
    for j in range(N-1):
        if s[i][j] != s[i][j+1]:
            tmp = s[i][j]
            s[i][j] = s[i][j+1]
            s[i][j+1] = tmp

            res = max(res, check(s))

            tmp = s[i][j]
            s[i][j] = s[i][j+1]
            s[i][j+1] = tmp

        if s[j][i] != s[j+1][i]:
            tmp = s[j][i]
            s[j][i] = s[j+1][i]
            s[j+1][i] = tmp

            res = max(res, check(s))

            tmp = s[j][i]
            s[j][i] = s[j+1][i]
            s[j+1][i] = tmp

print(res)