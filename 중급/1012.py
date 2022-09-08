from collections import deque
movex = [0,1,0,-1]
movey = [1,0,-1,0]
num = int(input())
list1 = []
def bfs(maze, x,y):
    queue = deque()
    queue.append((x,y))
    maze[y][x] = 0
    while queue:  
        x,y = queue.popleft()
        for i in range(4):
            nx = x + movex[i]
            ny = y + movey[i]
            if nx >= M or ny >= N or nx < 0 or ny < 0:
                continue
            if maze[ny][nx] == 1:
                maze[ny][nx] = 0
                queue.append((nx,ny))
for _ in range(num):
    count = 0
    M,N,K = map(int,input().split())
    maze = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        maze[y][x] = 1
        # queue.append((x,y))
        # # 큐 안에 배추 있는곳만 들어가게 함. 
    for i in range(M):
        for j in range(N):
            if maze[j][i] == 1:
                bfs(maze,i,j)
                count+=1
    list1.append(count)
for i in range(len(list1)):
    print(list1[i])



# while queue:  
    #     count = 0 
    #     x,y = queue.popleft()
    #     # maze[y][x] = 0
    #     for i in range(4):
    #         nx = x + movex[i]
    #         ny = y + movey[i]
    #         if nx >= M or ny >= N or nx < 0 or ny < 0:
    #             continue
    #         if maze[ny][nx] == 1:
    #             maze[ny][nx] == 0
    #             queue.append((x,y))
        #     if maze[ny][nx] == :
        #         count += 1
        # if count == 4: # 그냥 모두 다 0인 경우 
        #     result += 1
        # if count == 2: # 모서리인 경우  
        #     if x == M-1 and y == N-1:
        #         result += 1
        #     if x == 0 and y == 0:
        #         result += 1
        #     if x == 0 and y == N-1:
        #         result += 1
        #     if y == 0 and x == M-1:
        #         result += 1
        # if count == 3: # 벽면인 경우 
        #     if x == M-1 or y == N-1 or x == 0 or y == 0:
        #         result += 1