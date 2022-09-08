stack = []
list1 = list(input())
sum = 0 
j = 0
result = 1 
for i in list1:
    if i == '(':
        stack.append(i)
        result *= 2
    if i == '[':
        stack.append(i)
        result *= 3
    if i == ')':
        if not stack or stack[-1] == '[' :
            sum = 0
            break
        elif list1[j-1] == '(':
            sum += result
        result = result // 2
        stack.pop()
    if i == ']':
        if not stack or stack[-1] == '(' :
            sum = 0
            break
        elif list1[j-1] == '[':
            sum += result
        result = result // 3
        stack.pop()
    j += 1
if stack:
    print(0)
else:
    print(sum)