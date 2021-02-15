n = int(input())
s = [[0]*n for _ in range(n)]

def preorder(a):
    print(a, end="")
    if s[ord(a)-65][1] != ".":
        preorder(s[ord(a)-65][1])
    if s[ord(a)-65][2] != ".":
        preorder(s[ord(a)-65][2])
def inorder(a):
    if s[ord(a)-65][1] != ".":
        inorder(s[ord(a)-65][1])
    print(a, end="")
    if s[ord(a)-65][2] != ".":
        inorder(s[ord(a)-65][2])
def postorder(a):
    if s[ord(a)-65][1] != ".":
        postorder(s[ord(a)-65][1])
    if s[ord(a)-65][2] != ".":
        postorder(s[ord(a)-65][2])
    print(a, end="")

for _ in range(n):
    one, two, three = map(str, input().split())
    one_ = ord(one) - 65
    s[one_][0], s[one_][1], s[one_][2] = one, two, three

preorder("A")
print()
inorder("A")
print()
postorder("A")
print()