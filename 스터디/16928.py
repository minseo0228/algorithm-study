from collections import deque
N, M = map(int, input().split())
l  = []
graph = [101]*101
for _ in range(N+M):
    l.append(list(map(int,input().split())))
def bfs(v):
    queue = deque()
    queue.append(v)
    graph[v] = 0
    while queue:
        x = queue.popleft()
        if x == 100:
            print(graph[100])
            break
        for a, b in l:
                if x == a:
                    x = b
                    if graph[b] >= graph[a]:
                        graph[b] = graph[a]
                        queue.append(x)
                    continue
        for i in range(6):
            nx = x + (i+1)
            if nx < 101 :
                if graph[nx] > graph[x] +1 :
                    queue.append(nx)
                    graph[nx] = graph[x] +1
bfs(1)