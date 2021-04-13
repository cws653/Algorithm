from collections import deque
max = 100001
check = [False] * max
dist = [-1] * max

n,k = map(int, input().split())
q = deque()
q.append(n)
check[n] = True
dist[n] = 0

while q:
    now = q.popleft()
    if now*2 <= max and check[now*2] == False:
        q.appendleft(now*2)
        check[now*2] = True
        dist[now*2] = dist[now]
    if now + 1 <= max and check[now+1] == False:
        q.append(now+1)
        check[now+1] = True
        dist[now+1] = dist[now] + 1
    if now - 1 >= 0 and check[now-1] == False:
        q.append(now - 1)
        check[now-1] = True
        dist[now-1] = dist[now] + 1
print(dist[k])