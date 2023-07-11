from collections import deque
q = deque()
list1 = list(input())
count = 0
for i in list1:
    if i == '(':
        q.append(i)
    elif i == ')':
        if len(q) == 0:
            count += 1
        else :
            q.popleft()
print(count+len(q))
            