from collections import deque
k = int(input())
w,h = map(int,input().split())
graph = []
for i in range(h):
    graph.append(list(map(int, input().split())))

visit = [[[0]*(k+1) for _ in range(w)]for _ in range(h)]
monkeyx = [0,1,0,-1]
monkeyy = [1,0,-1,0]
horsex = [-2,-1,1,2,-2,-1,1,2]
horsey = [1,2,2,1,-1,-2,-2,-1]
def bfs(x,y,k):
    q = deque()
    q.append((x,y,k))
    while q:
        x,y,k = q.popleft()
        if x == h-1 and y == w-1:
            return(visit[x][y][k])
        if k > 0:
            for i in range(8):
                nx = horsex[i] + x
                ny = horsey[i] + y
                if nx < 0  or ny < 0 or nx >= h or ny >=w:
                    continue
                if graph[nx][ny] == 0 and visit[nx][ny][k-1]==0:
                        visit[nx][ny][k-1] = visit[x][y][k] + 1
                        q.append((nx,ny,k-1))
                        continue
        for i in range(4):
            nx = monkeyx[i] + x
            ny = monkeyy[i] + y
            if nx < 0  or ny < 0 or nx >= h or ny >=w:
                    continue
            if graph[nx][ny] == 0 and visit[nx][ny][k] == 0:
                    visit[nx][ny][k] = visit[x][y][k] + 1
                    q.append((nx,ny,k))
    return(-1)

print(bfs(0,0,k))



            