from collections import deque
N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
result = [100]*(N+1)
visit = [0]*(N+1)
def bfs(x):
    queue = deque()
    visit[x] = 1
    queue.append(x)
    while(queue):
        a = queue.popleft()
        numlist = graph[a]
        for i in numlist:
            if visit[i] == 0: #방문하지 않은 경우 
                visit[i] = visit[a] + 1 #저번 방문한거랑 +시켜 -> 이렇게 하면 방문 표시도 가능하고 베이컨 수도 확인 가능
                queue.append(i)
    # print(str(x)+':'+str(visit))

          
# 1부터 N까지 bfs돌려서 케빈 수 찾기 
for i in range(1,N+1):
    visit = [0]*(N+1)
    bfs(i)
    result[i] = (sum(visit))
print(result.index(min(result)))