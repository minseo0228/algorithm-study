from collections import deque
a,b = map(int,input().split())
graph = []
for i in range(a):
    graph.append(list(input()))
visit = [[0]*b for _ in range(a)]
movex = [0,1,0,-1]
movey = [1,0,-1,0] 
gsheep = 0
gwolf = 0

def bfs(x,y):
    global gwolf
    global gsheep
    sheep = 0
    wolf = 0
    q = deque()
    q.append((x,y))
    visit[x][y] = 1
    if graph[x][y] == 'v':
        wolf += 1
    if graph[x][y] == 'k':
        sheep += 1
    while q:
        x,y =q.popleft()
        for i in range(4):
            nx = x + movex[i]
            ny = y + movey[i]
            if nx >= a or ny >= b or nx < 0 or ny < 0:
                continue
            if visit[nx][ny] == 0 and graph[nx][ny] != '#':
                if graph[nx][ny] == 'v':
                    wolf += 1
                if graph[nx][ny] == 'k':
                    sheep += 1
                visit[nx][ny] = 1
                q.append((nx,ny))
    if sheep > wolf :
        gsheep += sheep
    else :
        gwolf += wolf

for i in range(a):
    for j in range(b):
            if graph[i][j] != '#' and visit[i][j] == 0:
                # 한번도 가보지 못한 새로운 울타리 안
                bfs(i,j)      
print(gsheep,gwolf)