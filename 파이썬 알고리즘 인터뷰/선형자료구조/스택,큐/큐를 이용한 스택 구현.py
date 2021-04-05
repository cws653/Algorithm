import collections

q = collections.deque()

def push(x):
    q.append(x)
    for _ in range(len(q) - 1):
        q.append(q.popleft())

def pop():
    return q.popleft()

def top():
    return q[0]

def empty():
    if deque.count() == 0:
        return False
    else:
        return True

push(1)
print(q)
push(2)
print(q)
print(pop())