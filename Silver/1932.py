n = int(input())
graph = []
dp = [[0]*(i) for i in range(1,n+1)]
for i in range(n):
    graph.append(list(map(int,input().split())))
dp[0][0]= graph[0][0]
for i in range(1,n):
    dp[i][0] = dp[i-1][0] + graph[i][0]
    dp[i][-1] = dp[i-1][-1] + graph[i][-1]
    for j in range(1,i-1):
        dp[i][j] = max(dp[i-1][j-1] + graph[i][j], dp[i-1][j] + graph[i][j])
print(max(dp[n-1]))
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(x+1) for x in range(n)]
for i in range(n-1):
    for j in range(len(arr[i])):
        if i ==0 :
            dp[i+1][j] = arr[i][j] + arr[i+1][j]
            dp[i+1][j+1] = arr[i][j] + arr[i+1][j+1]
        else:
            if dp[i+1][j] < dp[i][j] + arr[i+1][j]:
                dp[i+1][j] = dp[i][j] + arr[i+1][j]
            dp[i+1][j+1] = dp[i][j] + arr[i+1][j+1]

if n == 1: # 1일때는 for문을 타지 않기 때문에 따로 분기처리
    print(arr[0][0])
else:
    result = max(dp[n-1])
    print(result)