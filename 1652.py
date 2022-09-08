num = int(input())
maze = []
list1 = []
for _ in range(num):
    maze.append(list(map(str,input())))
r = 0
c = 0
for i in range(num):
    if num <= 1:
        break
    for j in range(num):
        if maze[i][j] == 'X':
            list1.append(j)
    # print(list1)
    if len(list1) == 0:
        r = r+1
    else:
        if list1[0] - 0 >= 2:
            r = r+1
        if (num-1) - list1[len(list1)-1] >=2:
            r = r+1
        for k in range(len(list1)):
            if k+1 == len(list1):
                break
            else:
                if list1[k+1] - list1[k] >2:
                    r = r+1
    list1 = []
for i in range(num):
    if num <= 1:
        break
    for j in range(num):
        if maze[j][i] == 'X':
            list1.append(j)
    # print(list1)
    if len(list1) == 0:
        c = c+1
    else:
        if list1[0] - 0 >= 2:
            c = c+1
        if (num-1) - list1[len(list1)-1] >=2:
            c = c+1
        for k in range(len(list1)):
            if k+1 == len(list1):
                break
            else:
                if list1[k+1] - list1[k] >2:
                    c = c+1
    list1 = []
print(r,c)
