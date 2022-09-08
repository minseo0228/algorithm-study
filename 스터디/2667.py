from collections import deque
N = int(input())
maze = []
for _ in range(N):
    maze.append(list(map(int,input())))
movex = [1,0,-1,0]
movey = [0,1,0,-1]
answer = []
def bfs(maze,x,y):
    counthouse = 0
    queue = deque()
    queue.append((x,y))
    maze[x][y] = 0
    while queue:
        x,y= queue.popleft()
        for i in range(4):
            nx = x + movex[i]
            ny = y + movey[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if maze[nx][ny] == 1:
                queue.append((nx,ny))
                maze[nx][ny] = 0
                counthouse += 1
    answer.append(counthouse)
count = 0
for i in range(N):
    for j in range(N):
        if maze[i][j] == 1:
            bfs(maze,i,j)
            count += 1
print(count)
answer.sort()
for i in range(len(answer)):
    print(answer[i]+1)