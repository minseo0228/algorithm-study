from collections import deque
N = int(input())
for i in range(N):
    queue = deque()
    list1 = input()
    flag = 0
    for i in list1:
        if i == "(":
            queue.append(i)
        elif i == ')':
            if len(queue) == 0:
                flag = 1
                break 
            else:
                queue.pop()
    if len(queue)==0 and flag == 0:
        print("YES")
    else:
        print("NO")