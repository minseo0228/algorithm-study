list1 = input()
N = int(input())
lenlist = len(list1)
cur = lenlist #현재 위치 

list3 = []
for i in range(N):
    list2 = list(input())
    list3.append(list2)

for i in range(N):
    list4 = list3[i]
    if list4[0] == 'L':
       if cur != 0:
        cur = cur - 1  
    elif list4[0] == 'D':
        if cur < len(list1):
           cur = cur + 1  
    elif list4[0] == 'B':
        if cur != 0:
            list1 = list1[:cur]+list1[cur+1:]
    else: 
        list1 = list1[:cur+1]+list4[2]+list1[cur+1:]

print(list1)