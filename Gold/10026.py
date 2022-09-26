from collections import deque
N = int(input())
graph = []
for i in range(N):
    graph.append(list(input()))
visit = [[0 for _ in range(N)]for _ in range(N)]
movex = [1,0,-1,0]
movey = [0,1,0,-1]
count1 = 0
def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    visit[a][b] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = movex[i] + x
            ny = movey[i] + y
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] == graph[x][y] and visit[nx][ny] == 0:
                queue.append((nx,ny))
                visit[nx][ny] = 1
def RtoG():
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'R':
                graph[i][j] = 'G'

for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            bfs(i,j)
            count1+=1
count = 0
visit = [[0 for _ in range(N)]for _ in range(N)]
RtoG()
for i in range(N):
    for j in range(N):
       if visit[i][j] == 0:
            bfs(i,j)
            count+=1
print(count1, count)   