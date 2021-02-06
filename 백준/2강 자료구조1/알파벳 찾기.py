input = input()

answear = [-1] * 26

for i in input:
    # print(input.index(i))
    answear[ord(i) - 97] = input.index(i)

print(answear)