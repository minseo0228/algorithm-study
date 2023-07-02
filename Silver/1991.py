from collections import deque
a,b = map(int,input().split())
graph = []
for i in range(a):
    graph.append(list(input()))
visit = [[0]*b for _ in range(a)]
movex = [0,1,0,-1]
movey = [1,0,-1,0]
def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x,y =q.popleft()
        for i in range(4):
            nx = x + movex[i]
            ny = y + movey[i]
            if visit[ny][nx] == 0:
                if graph[ny][nx] != '#'