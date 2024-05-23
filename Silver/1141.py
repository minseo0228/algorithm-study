n = int(input())
wordlist = []
for _ in range(n):
    wordlist.append(input())
wordlist.sort(key = lambda x : len(x))
# print(wordlist)
removeword = []
for i in range(len(wordlist)):
    count = 0
    wordlen = len(wordlist[i])
    for j in range(i+1, len(wordlist)):
        w = wordlist[j]
        # print("--",w)
        if w[:wordlen] == wordlist[i]:
            removeword.append(wordlist[i])
            break
# print(removeword)
print(len(wordlist)-len(removeword))
