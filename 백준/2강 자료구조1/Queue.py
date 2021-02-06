import sys

N = int(sys.stdin.readline())

queue = []

for i in range(N):
    input = sys.stdin.readline().split()

    if input[0] == "push":
        queue.insert(0, input[1])
    elif input[0] == "pop":
        if len(queue) != 0:
            print(queue.pop(0))
        else:
            print(-1)
    elif input[0] == "size":
        print(len(queue))
    elif input[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif input[0] == "front":
        if len(queue) != 0:
            print(queue[len(queue) - 1])

        else:
            print(-1)
    elif input[0] == "back":
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
