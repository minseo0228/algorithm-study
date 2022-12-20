prob, num = map(int,input().split())
pomon = {}
pomon1 = []
for i in range(prob):
    name = input()
    pomon[name] = i+1
    pomon1.append(name)
for i in range(num):
    name = input()
    if (name.isalpha()):
        print(pomon[name])
    else:
        name = int(name)
        print(pomon1[name-1])
