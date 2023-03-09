N,M = map(int,input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))

from collections import deque
movex = [0,1,0,-1]
movey = [1,0,-1,0]
def bfs(x,y):
    visit = [[0]*M for _ in range(N)]
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + movex[i]
            ny = y + movey[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 0:
                visit[nx][ny] = min(visit[nx][ny], visit[x][y]+1)
                q.append((nx,ny))
    print(visit)
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            bfs(i,j)
    