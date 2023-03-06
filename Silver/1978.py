N = int(input())
numlist = list(map(int,input().split()))
result = 0
for i in numlist:
    count = 0
    if i == 2:
        result += 1
    if i > 2:
        for j in range(1,i+1):
            if i % j != 0:
                count += 1
        print(count)
        if count == i-2:
            result += 1
print(result)