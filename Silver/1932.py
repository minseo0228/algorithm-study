n = int(input())
graph = []
dp = [[0]*(i) for i in range(1,n+1)]
for i in range(n):
    graph.append(list(map(int,input().split())))
dp[0][0]= graph[0][0]
# for i in range(1,n):
#     dp[i][0] = dp[i-1][0] + graph[i][0]
#     dp[i][-1] = dp[i-1][-1] + graph[i][-1]
#     for j in range(1,i-1):
#         dp[i][j] = max(dp[i-1][j-1] + graph[i][j], dp[i-1][j] + graph[i][j])
# print(max(dp[n-1]))
for j in range(1,n):
    for i in range(len(graph[j])):
        if i == 0:
            dp[j][0] = dp[j-1][0] + graph[j][0]
        elif i == len(graph[j])-1:
            dp[j][-1] = dp[j-1][-1] + graph[j][-1]
        else:
            dp[j][i] = max(dp[j-1][i-1] + graph[j][i], dp[j-1][i] + graph[j][i])
print(max(dp[-1]))