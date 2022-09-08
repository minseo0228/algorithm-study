from collections import deque
import sys
M,N,H = map(int,input().split())
graph = [[list(map(int,sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
movex = [0,0,0,0,-1,1]
movey = [0,1,0,-1,0,0]
movez = [1,0,-1,0,0,0]
visit = [[[0 for _ in range(M)]for _ in range(N)]for _ in range(H)]

queue = deque()
def bfs():
    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            nx = x + movex[i]
            ny = y + movey[i]
            nz = z + movez[i]
            if nx < 0 or ny < 0 or nx >= H or ny >= N or nz < 0 or nz >= M:
                continue
            if graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = 1 
                visit[nx][ny][nz] = visit[x][y][z] + 1
                queue.append((nx,ny,nz))
#처음에 있는 토마토 위치 다 파악하고 다 queue 돌려
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))
#visit 그래프에 0이 있으면 토마토가 모두 익을 수 없는 경우 
bfs()
flag = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if visit[i][j][k] == 0 and graph[i][j][k] == 0 :
                flag += 1

answer = -1
if flag == 0:
    for i in range(H):
        for j in range(N):
            for k in range(M):
                answer = max( answer, visit[i][j][k])
    print(answer)
else:
    print(-1)
