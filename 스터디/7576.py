from collections import deque
M,N = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
movex = [1,0,-1,0]
movey = [0,1,0,-1]
visit = [[0]*M for _ in range(N)]
queue = deque()
def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + movex[i]
            ny = y + movey[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1 
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx,ny))
#처음에 있는 토마토 위치 다 파악하고 다 queue 돌려
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i,j))
#visit 그래프에 0이 있으면 토마토가 모두 익을 수 없는 경우 
bfs()
flag = 0
for i in range(N):
    for j in range(M):
        if visit[i][j] == 0 and graph[i][j] == 0 :
            flag += 1
if flag == 0:
    print(max(map(max,visit)))
else:
    print(-1)

