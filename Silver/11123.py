from collections import deque
N = int(input())

movex = [0,1,0,-1]
movey = [1,0,-1,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visit[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + movex[i]
            ny = y + movey[i]
            if 0<=nx<a and 0<=ny<b:
                if graph[nx][ny] == '#' and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    q.append((nx,ny)) 
for _ in range(N):
    graph = []
    count = 0
    a,b = map(int,(input().split()))
    visit = [[0]*b for _ in range(a)]
    for j in range(a):
        graph.append(list(input()))
    for i in range(a):
        for j in range(b):
            if graph[i][j] == '#' and visit[i][j] == 0:
                bfs(i,j)
                count += 1
    print(count)
    