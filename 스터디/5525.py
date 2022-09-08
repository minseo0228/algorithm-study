N = int(input())
M = int(input())
list1 = list(input().strip())
print(list1)
countp = 0
count = 0
for i in range(M- 2*N) :
    if list1[i] == 'I':
        countp = 0
        for j in range(2*N + 1):
            if (i+j) % 2 == 0:
                if list1[i+j] == 'I':
                    countp += 1
            else:
                if list1[i+j] == 'O':
                    countp += 1
        if countp == (2*N +1):
            count += 1
print(count)