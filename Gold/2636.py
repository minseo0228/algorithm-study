# from collections import deque
# n,m = map(int,input().split())
# graph = []
# cheeze = 0 #전체 치즈 수
# for i in range(n):
#     list1 = list(map(int,input().split()))
#     for j in list1:
#         if j == 1:
#             cheeze += 1
#     graph.append(list1)

# movex = [0,1,0,-1]
# movey = [1,0,-1,0]

# time = 0
# def bfs(x,y): #외부 공기와 접한 치즈를 녹이는 것 bfs한번에 한시간
#     visit =[[0]*m for _ in range(n)]
#     q = deque()
#     cheeze_melt = []
#     q.append((x,y))
#     while q:
#         x,y = q.popleft()
#         for i in range(4):
#             nx = x + movex[i]
#             ny = y + movey[i]
#             # if nx < 0 or ny < 0  or nx >= n or ny >= m:
#             #     continue
#             # # if 0<=nx<n and 0<=ny<m:
#             # if graph[nx][ny] == 0 and visit[nx][ny] == 0:
#             #     visit[nx][ny] = 1
#             #     q.append([nx,ny])
#             # elif graph[nx][ny] == 1 and visit[nx][ny] == 0:
#             #     visit[nx][ny] = 1
#             #     cheeze_melt.append((nx,ny))
#             if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
#                 visit[nx][ny] = 1
#                 if graph[nx][ny] == 0:  # 공기면 계속 탐색하기 위해 큐에 넣음
#                     q.append((nx, ny))
#                 elif gra[nx][ny] == 1:  # 치즈면 한 번에 녹이기 위해 melt에 넣음
#                     cheeze_melt.append([nx, ny])
#     c = len(cheeze_melt)
#     for i in range(c):
#         l = cheeze_melt[i]
#         a = l[0]
#         b = l[1]
#         graph[a][b] = 0
#     return c

# while True:
#     m = bfs(0,0) # -> break전이 모두 없어지기 한시간 전 
#     time += 1
#     cheeze -= m
#     if cheeze == 0:
#         print(time)
#         print(m)
#         break

from collections import deque
movex = [0,1,0,-1]
movey = [1,0,-1,0]
def bfs():
    visit = [[0]*m for _ in range(n)]
    q = deque()
    q.append((0,0))
    cheeze = deque()
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + movex[i]
            ny = y + movey[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    if graph[nx][ny] == 0:
                        q.append((nx,ny))
                    if graph[nx][ny] == 1:
                        cheeze.append((nx,ny))
    #cheeze 녹이기
    c = len(cheeze)
    for a,b in cheeze:
        graph[a][b] = 0
    return(c)

n,m = map(int,input().split())
graph = []
all_cheeze = 0 #전체 치즈 수
for i in range(n):
    graph.append(list(map(int,input().split())))
    all_cheeze += sum(graph[i])
time = 0
while True:
    count = bfs()
    time += 1
    all_cheeze -= count
    if all_cheeze == 0:
        print(time)
        print(count)
        break
