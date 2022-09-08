from collections import deque
M,N = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip())))
visit = [[0 for _ in range(M)]for _ in range(N)]
movex = [1,0,-1,0]
movey = [0,1,0,-1]
def bfs(a,b):
    count = 0
    queue = deque()
    queue.append((a,b))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + movex[i]
            ny = y + movey[i]
            if nx < 0 or ny < 0 or nx >=M or ny >= N:
                continue
            if graph[nx][ny] == 0 and not visit: #visit == 0인경우까지
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
            if graph[nx][ny] == 1:
                if count == 0:
