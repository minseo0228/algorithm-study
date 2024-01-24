N = int(input())
numlist = list(map(int,input().split()))
result = [1]*N
for i in range(N):
    start = numlist[i]
    for j in range(i+1,N):
        next = numlist[j]
        if start < next:
            result[j] = max(result[i]+1, result[j])
# print(result)
print(max(result))