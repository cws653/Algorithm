n = int(input())
s = input().split()
visited = [False]*10
mx, mn = "", ""

def possible(a,b,c):
    if c == "<":
        return a < b
    if c == ">":
        return a > b
    return True

def dfs(cnt, arr):
    global mx, mn
    if cnt == n+1:
        if not len(mn):
            mn = arr
        else:
            mx = arr
        return
    for i in range(10):
        if not visited[i]:
            if cnt == 0 or possible(arr[-1], str(i), s[cnt-1]):
                visited[i] = True
                dfs(cnt+1, arr+str(i))
                visited[i] = False

dfs(0,"")
print(mx)
print(mn)