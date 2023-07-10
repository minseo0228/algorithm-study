from collections import deque
n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
visit = [[[0]*2 for _ in range(m)]for _ in range(n)]
visit[0][0][0] = 1
movex = [0,1,0,-1]
movey = [1,0,-1,0]
def bfs(x,y,k):
    q = deque()
    q.append((x,y,k))
    while q:
        x,y,k = q.popleft()
        if x == n-1 and y == m-1:
            return(visit[x][y][k])
        for i in range(4):
            nx = movex[i] + x
            ny = movey[i] + y
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1 and k == 0:
                visit[nx][ny][1] = visit[x][y][0] + 1
                q.append((nx,ny,1))
                continue
            if graph[nx][ny] == 0 and visit[nx][ny][k] == 0:
                visit[nx][ny][k] = visit[x][y][k] + 1
                q.append((nx,ny,k))
       
    return(-1)

print(bfs(0,0,0))