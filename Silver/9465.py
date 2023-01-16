t = int(input())
for j in range(t):
    graph = []
    n = int(input())
    for i in range(2):
        list1 = list(map(int,input().split()))
        graph.append(list1)
    if n == 1:
        print(max(map(max,graph)))
    else:
        graph[1][1] = graph[0][0] + graph[1][1]
        graph[0][1] = graph[0][1] + graph[1][0]
        for i in range(2,n):
            graph[0][i] = max(graph[0][i-2] + graph[0][i], graph[0][i-1], graph[1][i-2] + graph[0][i], graph[1][i-1] + graph[0][i])
            graph[1][i] =  max(graph[1][i-2] + graph[1][i], graph[1][i-1], graph[0][i-2] + graph[1][i], graph[0][i-1] + graph[1][i])
        print(max(map(max,graph)))