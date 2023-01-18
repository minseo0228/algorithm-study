from collections import deque
movex = [0,1,0,-1,1,1,-1,-1]
movey = [1,0,-1,0,1,-1,1,-1]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visit[y][x] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x + movex[i]
            ny = y + movey[i]
            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue
            if visit[ny][nx] == 0 and graph[ny][nx] == 1:
                visit[ny][nx] = 1
                queue.append((nx,ny))
while(True):
    w,h= map(int,input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for i in range(h):
        graph.append(list(map(int,input().split())))
    visit = [[0]*w for _ in range(h)]
    count = 0
    for i in range(w):
        for j in range(h):
            if graph[j][i] == 1 and visit[j][i] == 0:
                bfs(i,j)
                count += 1
    print(count)