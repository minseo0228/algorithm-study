wordlist = list(input())
stack = []
result = []
check = 0

for i in wordlist:
    if i == '<':
        check = 1
        while stack:
            result.append(stack.pop())
    if check == 1:
        result.append(i)
    if i == '>':
        check = 0
        continue
    if check == 0:
        if i == ' ':
            while stack :
                result.append(stack.pop())
            result.append(i)
        else:
            stack.append(i)

while stack :
    result.append(stack.pop())
    
for i in result:
    print(i,end='')
