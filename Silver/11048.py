N,M = map(int,input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))
for i in range(N-1):
    graph[i+1][0] += graph[i][0]
for i in range(M-1):
    graph[0][i+1] += graph[0][i]
for i in range(1,N):
    for j in range(1,M):
        graph[i][j] = graph[i][j] + max(graph[i-1][j],graph[i][j-1],graph[i-1][j-1])
print(graph[N-1][M-1])
