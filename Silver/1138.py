N = int(input())
line = list(map (int,(input().split())))

result = [0]*N
for i in range(N):
    a = line[i]
    count = 0
    for j in range(N):
        if result[j] == 0 and count == a:
            result[j] = i +1 
            break
        else:
            if result[j] == 0:
                count += 1
    
for i in range(N):
    print(result[i], end =' ')