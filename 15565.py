a,b = map(int,(input().split()))
list1 = list(map(int,(input().split())))
list2 = []
list3 = []
for i in range(a):
    if list1[i] == 1:
        list2.append(i)
i = 0
while True:
    if (i+b-1) >= len(list2):
        break
    x = list2[i+b-1] - list2[i]
    list3.append(x)
    i = i+1
list3.sort()
if len(list3) == 0:
    print("-1")
else:
    print(list3[0]+1)