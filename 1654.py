a,b = map(int, input().split())
list1 = []
for i in range(a):
    list1.append(int(input()))
max = 1
i = 0
sum = 0
while True:
    for i in range(a):
        sum += list1[i]//max
    max += 1 
    if sum == b:
        sum = 0
        for i in range(a):
            sum += list1[i]//max
        if sum == b:
            sum =0
            continue
        else:
            print(max-1)
            break
    else:
        sum = 0
