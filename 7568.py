num = int(input())
list1 = []
for i in range(num):
    a = list(map(int, input().split()))
    list1.append(a)
count = 1
for i in range(num):
    for j in range(num):
        if list1[i][0] < list1[j][0]  and list1[i][1] < list1[j][1]:
            count += 1
    print(count)
    count =1
