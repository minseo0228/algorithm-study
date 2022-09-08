from collections import deque
num = int(input())
movex = [1,-1,1,-1,2,2,-2,-2]
movey = [2,2,-2,-2,1,-1,1,-1]
def bfs(graph, x, y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 1
    while queue:
        x,y = queue.popleft()
        if (x == fx and y == fy):
            print(graph[x][y]-1)
            break
        for j in range(8):
            nx = movex[j] + x
            ny = movey[j] + y
            if (ny < 0 or nx < 0 or ny >= a or nx >= a):
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
for i in range(num):
    a = int(input())
    sx,sy = map(int, input().split())
    fx,fy = map(int, input().split())
    graph = [[0]*a for _ in range(a)]
    bfs(graph, sx, sy)
    