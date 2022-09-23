T = int(input())
for _ in range(T):
    num = int(input())
    dic = {}
    result = 1
    for i in range(num):
        clothes, type = input().split()
        if type in dic:
            temp = dic[type]
            dic[type] = temp + 1
        else:
            dic[type] = 1
    listnum = list(dic.values())
    for i in range(len(listnum)):
        result = result * (listnum[i]+1)

    print(result-1)