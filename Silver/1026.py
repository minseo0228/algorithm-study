N = int(input())
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
sum = 0
list1.sort()
list2.sort(reverse=True)
for i in range(N):
    sum += list1[i]*list2[i]
print(sum)