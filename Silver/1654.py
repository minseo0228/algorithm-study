K,N = map(int,input().split())
list1 = []
for i in range(K):
    list1.append(int(input()))
list1.sort()
start = 1
end = max(list1)
 
while(start<=end):
    mid = (start+end)//2
    cnt = 0
    for i in list1:
        cnt += i//mid
    if cnt>= N: 
        start = mid+1
    else:
        end = mid-1
print(end)