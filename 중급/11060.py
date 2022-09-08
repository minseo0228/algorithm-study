num = int(input())
list1 = list(map(int,input().split()))
dp =[1]*num
list2 = []
for i in range(num):
    for j in range(list1[i]-1):
        list2 = dp
        dp[i+j] = dp[i] + 1
        dp[i+j] = min(dp[i+j],list2[i+j])
        print(dp)