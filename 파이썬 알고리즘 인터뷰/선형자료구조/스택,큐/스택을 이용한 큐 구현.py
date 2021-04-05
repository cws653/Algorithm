import collections
q = collections.deque()

input = []
output = []

def push(x):
    input.append(x)

def pop():
    peek()
    return output.pop()

def peek():
    if not output:
        while input:
            output.append(input.pop())
    return output[-1]

def empty():
    return input == [] and output == []

