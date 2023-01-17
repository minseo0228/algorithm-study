from collections import deque
N = int(input())
graph = []
for i in range(N):
    graph.append(list(input()))

result = []
movex = [0,1,0,-1]
movey = [1,0,-1,0]
def bfs(x):
    visit = [0]*N
    count = 0
    queue = deque()
    queue.append((x,0))
    visit[x] = 1
    while queue:
        x,c = queue.popleft()
        if c >= 2: #2보다 멀어지면 친구가 될 수 없아..
            continue
        for i in range(N):
            if visit[i] == 0 and graph[i][x] == 'Y':
                visit[i] = 1
                queue.append((i,c+1))
                count += 1
    result.append(count)

for i in range(N):
    bfs(i)
print(max(result))      