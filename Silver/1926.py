from collections import deque
a,b = map(int,input().split())
graph = []
for i in range(a):
    graph.append(list(map(int,(input().split()))))
visit = [[0]*b for _ in range(a)]

mmax = 0
movex = [0,1,0,-1]
movey = [1,0,-1,0]
def bfs(x,y):
    global mmax
    count = 1
    q = deque()
    q.append((x,y))
    visit[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + movex[i]
            ny = y + movey[i]
            if nx < 0 or ny < 0 or nx >= a or ny >= b:
                continue
            if graph[nx][ny] == 1 and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                count += 1
                q.append((nx,ny))
    mmax = max(mmax,count)

gcount = 0
for i in range(a):
    for j in range(b):
        if graph[i][j] == 1 and visit[i][j] == 0:
            bfs(i,j)
            gcount += 1
print(gcount)
print(mmax)