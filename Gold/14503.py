N,M = map(int,input().split())
r,c,d = map(int,input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))
visit = [[0]*(N) for _ in range(M)]
def level1(x,y,d,count):
    if 0 <= x < N and 0 <= y <M:
        if visit[x][y] == 0:
            visit[x][y] = 1
            count += 1
        level2_5(x,y,d,count)

def turn(d):
    d = d - 1
    if d < 0:
        d = 3
    return(d)

movey = [0,1,0,-1]
movex = [-1,0,1,0]
def level2_5(x,y,d,count):
    check = 1
    for i in range(4):
        nx = x + movex[i]
        ny = y + movey[i]
        if 0 <= nx < N and 0 <= ny <M:
            if graph[nx][ny] == 0 and visit[nx][ny] == 0:
                check = 0
                level3(x,y,d,count)
    if check == 1:
        level2(x,y,d,count)
        
def level2(x,y,d,count):
    nx = x - movex[d]
    ny = y - movey[d]
    if 0 <= nx < N and 0 <= ny <M:
        if graph[nx][ny] == 1:
            print(count)
            quit()
        else:
            level1(nx,ny,d,count)
    
def level3(x,y,d,count):
    while True:
        d = turn(d)
        nx = x + movex[d]
        ny = y + movey[d]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0 and visit[nx][ny] == 0:
                level1(nx,ny,d,count)
                quit()

count = 1
visit[r][c] = 1
level1(r,c,d,count)