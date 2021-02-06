# word_s = input()
# word_count_dic = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,
#                   'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,
#                   'w':0,'x':0,'y':0,'z':0}
# index = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
#          's','t','u','v','w','x','y','z',]
#
# for word in word_s:
#     word_count_dic[word] += 1
#
# for idx in index:
#     print(word_count_dic[idx], end=" ")

str = input()

result = [0] * 26
# print(result)

for i in str:
    print(ord(i))
    result[ord(i) - 97] = str.count(i)

for i in result:
    print(i, end=" ")

