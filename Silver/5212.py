R,C = map(int,(input().split()))

movex = [1,0,-1,0]
movey = [0,1,0,-1]
graph = []
visit = [['.']*C for _ in range(R)]
# print(visit)
for i in range(R):
    graph.append(list(input()))
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'X':
            visit[i][j] = 'X'
        
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'X':
            count = 0
            for k in range(4):
                nx = i + movex[k]
                ny = j + movey[k]
                if nx >= R or ny >= C or nx < 0 or ny < 0:
                    count += 1
                else:
                    if graph[nx][ny] == '.':
                    #  and visit[nx][ny] == 0:
                        count += 1
            if count >= 3 :
                visit[i][j] = '.'
                # visit[i][j] = 1

x = 0
y = 0
x1 = 100
y1 = 100
for i in range(R):
    for j in range(C):
        if visit[i][j] == 'X':
            x = max(x,i)
            x1 = min(x1,i)
            y = max(y,j)
            y1 = min(y1,j)

for i in range(x1,x+1):
    for j in range(y1,y+1):
        print(visit[i][j], end='')
    print()