import sys
N = int(sys.stdin.readline().strip())
ans = []

for i in range(N+1):
    for j in range(N+1-i):
        for k in range(N+1-i-j):
            t = N+1-i-j-k
            a = i*1 + j*5 + k*10 + t*50
            ans.append(a)
print(len(set(ans)))


# 2: 0 -> 0,1 / 1 -> 0

# def dfs(depth, s):
#     if depth == N:
#         check[s] = 1
#         return
#     for i in range(4):
#         dfs(depth + 1, s + nums[i])
#
# N = int(input().strip())
# nums = [1,5,10,50]
# check = [0]*(50*20+1)
# dfs(0,0)
# cnt = 0
# for i in check:
#     if i:
#        cnt += 1
# print(cnt)