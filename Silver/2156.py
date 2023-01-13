n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))
dp = [0]*(n+10)
dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
dp[2] = max(wine[0]+wine[2],wine[0]+wine[1],wine[1]+wine[2])
for i in range(3,n):
    dp[i] = max(dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i],dp[i-1])
# print(max(dp))
print(dp)