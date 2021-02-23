# ROT13이 기존 문자에 아스키코드 13을 더하는 것이다.
s = str(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

answear = ''
for i in s:
    if i == ' ':
        answear += i
        continue
    try:
        answear += str(int(i))
    except:
        if i in alphabet:
            x = alphabet.index(i)
            if x > 12:
                answear += alphabet[x-13]
            else:
                answear += alphabet[x+13]
        else:
            x = ALPHABET.index(i)
            if x > 12:
                answear += ALPHABET[x-13]
            else:
                answear += ALPHABET[x+13]
print(answear)