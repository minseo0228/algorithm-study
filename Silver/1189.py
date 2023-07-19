from collections import deque
r,c,k = map(int,input().split())
graph = []
for i in range(r):
    graph.append(list(input()))
visit = [[0]*c for _ in range(r)]
movex = [0,1,0,-1]
movey = [1,0,-1,0]
result = 0
def bfs(x,y,k):
    global result
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        if x == c-1 and y == r-1 and visit[x][y] == k:
            result += 1
        visit[x][y] = 1
        for i in range(4):
            nx = x + movex[i]
            ny = y + movey[i]
            if nx < 0 or ny < 0 or nx >= c or ny >= r:
                continue
            if graph[nx][ny] == 'T' and visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx,ny))

bfs(0,0,k)  
print(result)
    
