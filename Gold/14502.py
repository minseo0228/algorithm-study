# from collections import deque
# # from itertools import combinations
# import copy
# n,m = map(int,input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int,input().split())))
# # 1 벽 2 바이러스 
# movex = [0,1,0,-1]
# movey = [1,0,-1,0]
# result = 0
# #바이러스 전파 
# def bfs():
#     global result
#     gra = copy.deepcopy(graph)
#     q = deque()
#     # visit = [[0]*m for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             if gra[i][j] == 2:
#                 q.append((i,j))
#     while q:
#         x,y = q.popleft()
#         # visit[x][y] = 1
#         for i in range(4):
#             nx = x + movex[i]
#             ny = y + movey[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >=m:
#                 continue
#             if gra[nx][ny] == 0 :
#                 gra[nx][ny] = 2
#                 q.append((nx,ny))
#     count = 0
#     for i in range(n):
#         for j in range(m):
#             # if gra[i][j] == 0 and graph[i][j] == 0:
#             if gra[i][j] == 0:
#                 count += 1
#     result = max(result,count)
# def wall(a):
#     if a == 3:
#         bfs()
#         return
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 0:
#                 graph[i][j] = 1
#                 wall(a+1)
#                 graph[i][j] = 0
# wall(0)
# print(result)
    
from collections import deque
from itertools import combinations
n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
# 1 벽 2 바이러스 
movex = [0,1,0,-1]
movey = [1,0,-1,0]
result = 0
#바이러스 전파 
def bfs(gra):
    global result
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q.append((i,j))
    while q:
        x,y = q.popleft()
        # visit[x][y] = 1
        for i in range(4):
            nx = x + movex[i]
            ny = y + movey[i]
            if nx < 0 or ny < 0 or nx >= n or ny >=m:
                continue
            if gra[nx][ny] == 0:
                gra[nx][ny] = 2
                q.append((nx,ny))
    count = 0
    print(gra)
    for i in range(n):
        for j in range(m):
            # if gra[i][j] == 0 and graph[i][j] == 0:
            if gra[i][j] == 0:
                count += 1
    result = max(result,count)

list0 = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            list0.append([i,j])
#벽 세우기
for i in combinations(list0,3):
    # gra = [[0]*m for _ in range(n)]
    gra = graph
    for j in range(3):
        x = i[j][0]
        y = i[j][1]
        gra[x][y] = 1
    bfs(gra)

print(result)
    

