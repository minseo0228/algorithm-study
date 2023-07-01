wordlist = list(input().split())
result = []
def word1(i):
    length = len(i)
    word = ''
    for j in range(length):
        word += i[length-j-1]
    result.append(word)
for i in wordlist:
    indexlist = []
    if '<' in i:
        indexlist.append(i.index('<'))
    print(indexlist)
    # length = len(i)
    # word = ''
    # for j in range(length):
    #     if i[j] == '<':
    #         while True:
    #             if 
    #     word += i[length-j-1]
    # result.append(word)
    

for i in result:
    print(i, end=' ')