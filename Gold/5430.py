T = int(input())
for _ in range(T):
    count = 0
    error = 0
    functionlist = list(input().strip())
    n = int(input())
    listnum = list((input().strip('[' ']').split(',')))
    if n == 0:
        listnum = []
    else:
        listnum = list(map(int, listnum))
    for i in functionlist:
        if i == 'R':
            count += 1
        if i == 'D':
            if len(listnum)== 0:
                error = 1
            else:
                if count %2 == 0:
                    listnum.pop(0)
                if count % 2 == 1:
                    listnum.pop()
    if error == 1:
        print("error")
    else:
        if count %2 == 0:
            print("[" + ",".join(map(str, listnum)) + "]")
        if count %2 == 1:
            listnum.reverse()
            print("[" + ",".join(map(str, listnum)) + "]")
