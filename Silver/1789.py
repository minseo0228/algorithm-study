a = int(input())
i = 1
flag = 1
while True:
    if a < 0:
        flag = flag-1
        break
    a = a-i
    flag = i
    i += 1  
print(flag)