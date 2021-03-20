def Palindrome(s: str) -> bool:
    strs = []
    for i in s:
        if i.isalnum():
            strs.append(i.lower())
    print(strs)
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

s = input()
print(Palindrome(s))