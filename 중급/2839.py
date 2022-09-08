num = int(input())
count =0
def sugar(num,count):
    while num>=0:
        if num % 5 == 0:
            num = num - 5
            count += 1
        elif num % 3 == 0:
            num = num - 3
            count += 1
    return count-1

if num%5==0 or num%3==0:
    print(sugar(num,count))
else:
    time = 0
    for i in range(1667):
        if time == 1:
            break
        for j in range(1000):
            if ((5*j) + (3*i)) == num:
                time = 1
                break
    if time == 1:
        print(i+j-1)
    else:
        print(-1) 

