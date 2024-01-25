n = int(input())
numlist = list(map(int,input().split()))
dp = [0]*n
for i in range(n):
    dp[i] = max(dp[i],numlist[i])
    start = numlist[i]
    for j in range(i+1,n):
        next = numlist[j]
        if start < next:
            dp[j] = max(dp[i]+next, dp[j])
        # print(dp)
print(max(dp))