list = []
while True:
    num = input()
    list.append(num)
    if num == '0':
        break

for i in range(len(list)-1):
    a = list[i]
    if len(a) == 5:
        if a[0]==a[4] and a[1]==a[3]:
            print("yes")
        else:
            print("no")
    elif len(a) == 4:
        if a[0]==a[3] and a[1]==a[2]:
            print("yes")
        else:
            print("no")
    elif len(a) == 3:
        if a[0]==a[2]: 
            print("yes")
        else:
            print("no")
    else:
        print("yes")