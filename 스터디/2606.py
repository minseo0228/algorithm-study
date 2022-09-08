from collections import deque
num = int(input())
edge = int(input())
graph = [[0]*(num+1) for _ in range(num+1)]
visit = [0]*(num+1)

def bfs(V):
    count = 0
    queue = deque()
    queue.append(V)
    visit[V] = 1
    while queue:
        V = queue.popleft()
        for i in range(1, num+1):
            if visit[i] == 0  and graph[V][i] == 1:
                queue.append(i)
                visit[i] = 1
                count += 1
    return count

for i in range(edge):
    x,y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

print(bfs(1))