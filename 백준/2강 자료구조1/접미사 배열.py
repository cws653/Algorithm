input = input()
input = list(input)
myStrings = []

for i in range(len(input)):
    myStrings.append(''.join(input))
    input.pop(0)

result = sorted(myStrings)

for word in result:
    print(word)

