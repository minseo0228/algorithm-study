N = int(input())
numlist = list(map(int,input().split()))
result = []
for i in range(N):
    length = 1
    start = numlist[i]
    for j in range(i+1,N):
        if start < numlist[j]:
            length += 1
            start = numlist[j]
    result.append(length)
print(max(result))