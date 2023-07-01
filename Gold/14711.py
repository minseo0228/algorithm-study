from collections import deque
N = int(input())
graph = [['.']*N for _ in range(N)]
result = [['.']*N for _ in range(N)]
first = list(input())
for i in range(N):
    graph[0][i] = first[i]
    result[0][i] = first[i]

movex = [0,1,0,-1]
movey = [1,0,-1,0]

for i in range(N):
    if graph[0][i] == '#':
        for j in range(4):
            nx = i + movex[j]
            ny = 0 + movey[j]
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny] == '.':
                    graph[nx][ny] = '#'
                elif graph[nx][ny] == '#':
                    graph[nx][ny] = '.'

for i in range(1,N):
    for j in range(N):
        if graph[i][j] == '.':
            check = 0
            for k in range(4):
                nx = i + movex[k]
                ny = j + movey[k]       
                if 0<=nx<N and 0<=ny<N:
                    if graph[nx][ny] == '#':
                        check = 1
                        break
            if check == 1:
                result[i][j] = '#'
            for k in range(4):
                nx = i + movex[k]
                ny = j + movey[k]
                if 0<=nx<N and 0<=ny<N: 
                    if graph[nx][ny] == '.':
                        graph[nx][ny] = '#'
                    elif graph[nx][ny] == '#':
                        graph[nx][ny] = '.'

print(result)