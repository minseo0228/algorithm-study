from collections import deque
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
movex = [0,1,0,-1]
movey = [1,0,-1,0]

min_val = min(map(min,graph))
max_val = max(map(max,graph))
result = 0

for i in range(0,max_val+1):
    count = 0
    q = deque()
    visit = [[0]*n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visit[j][k] == 0:
                visit[j][k] = 1
                q.append((j,k))
                while q:
                    x,y = q.popleft()
                    for u in range(4):
                        nx = x + movex[u]
                        ny = y + movey[u]
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        if visit[nx][ny] == 0 and graph[nx][ny] > i:
                            visit[nx][ny] = 1
                            q.append((nx,ny))
                count += 1
    result = max(result,count)
print(result)
    
