from collections import deque
r,c = map(int,input().split())
graph = []
for i in range(r):
    graph.append(list(input()))
visit = [[0]*c for _ in range(r)]
gwolf = 0
gsheep = 0
movex = [0,1,0,-1]
movey = [1,0,-1,0]
def bfs(x,y):
    global gwolf
    global gsheep
    wolf = 0
    sheep = 0
    q = deque()
    q.append((x,y))
    visit[x][y] = 1
    if graph[x][y] == 'v':
        wolf += 1
    if graph[x][y] == 'o':
        sheep += 1 
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + movex[i]
            ny = y + movey[i]
            if nx < 0 or ny < 0 or nx >=r or ny >=c:
                continue
            if visit[nx][ny] == 0 and graph[nx][ny]!= '#':
                if graph[nx][ny] == 'v':
                    wolf += 1
                if graph[nx][ny] == 'o':
                    sheep += 1 
                visit[nx][ny] = 1
                q.append((nx,ny))
    if wolf >= sheep:
        gwolf += wolf
    else:
        gsheep += sheep

for i in range(r):
    for j in range(c):
        if visit[i][j] == 0 and graph[i][j] != '#':
            bfs(i,j)
print(gsheep,gwolf)