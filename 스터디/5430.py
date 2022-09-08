T = int(input())
for _ in range(T):
    error = 0
    functionlist = list(input().strip())
    n = int(input())
    if  n == 0:
        listnum = list(input().strip())
        listnum = []
    else:
        listnum = list((input().strip('[' ']').split(',')))
        listnum = list(map(int, listnum))
    if len(functionlist) > len(listnum):
        error = 1
    if error == 0:
        for i in functionlist:
            if i == 'R':
                listnum.reverse()
            if i == 'D':
                listnum.pop(0)
    if error == 1:
        print("error")
    else:
        print(listnum)