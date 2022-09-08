from collections import deque
maze = []
movex = [-1, 1]
movey = [-1, 1]
def bfs(maze,x,y):
    countx = 0
    county = 0
    queue = deque()
    queue.append((x,y))
    if maze[y][x] == '-':
        maze[y][x] = 1
        while queue:
            x,y = queue.popleft()
            for i in range(2):
                nx = x + movex[i]
                if nx < 0 or nx >= M :
                    continue
                if maze[y][nx] == '-':
                    maze[y][nx] = 1
                    queue.append((nx,y))
        countx += 1
    elif maze[y][x] == '|':
        maze[y][x] = 1
        while queue:
            x,y = queue.popleft()
            for i in range(2):
                ny = y + movey[i]
                if ny < 0 or ny >= N :
                    continue
                if maze[ny][x] == '|':
                    maze[ny][x] = 1
                    queue.append((x,ny))
        county+= 1
    return(countx + county)
N, M = map(int,input().split()) # N 세로 M 가로
for i in range(N):
    maze.append(list(input()))
result = 0
for i in range(M):
    for j in range(N):
        a = bfs(maze,i, j)
        result = result + a
print(result)
        