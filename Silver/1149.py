n = int(input())
m = []
for i in range(n):
    m.append(list(map(int, input().split())))

dp = [[[] for _ in range(n)] for _ in range(3)]
dp[0][0] = m[0][0]
dp[1][0] = m[0][1]
dp[2][0] = m[0][2]


for i in range(1,n):
    dp[0][i] = min(dp[1][i-1]+m[i][0], dp[2][i-1]+m[i][0])
    dp[1][i] = min(dp[0][i-1]+m[i][1], dp[2][i-1]+m[i][1])
    dp[2][i] = min(dp[1][i-1]+m[i][2], dp[0][i-1]+m[i][2])

print(min(dp[0][n-1],dp[1][n-1],dp[2][n-1]))