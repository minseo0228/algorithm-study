from collections import deque
N,M,V = map(int, input().split())
graph = [[0]*(N+1)for _ in range(N+1)]
visit = [0]*(N+1)
def dfs(V):
    visit[V] = 1
    print(V,end = " ")
    for i in range(1, N+1):
        if visit[i] == 0 and graph[V][i] == 1:
            dfs(i)
def bfs(V):
    queue = deque()
    queue.append(V)
    visit[V] = 1
    while queue:
        V = queue.popleft()
        print(V,end = " ")
        for i in range(1, N+1):
            if visit[i] == 0  and graph[V][i] == 1:
                queue.append(i)
                visit[i] = 1
for _ in range(M):
    x,y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1
dfs(V)
visit = [0]*(N+1)
print()
bfs(V)