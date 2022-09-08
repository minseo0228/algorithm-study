T = int(input())
for i in range(T):
    data = list(input().split())
    num = int(data[0])
    list1 = list(data[1])
    for j in range(len(list1)):
        for k in range(num):
            print(list1[j],end='')
    print("")