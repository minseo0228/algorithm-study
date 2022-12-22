N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visit = [0]*(N+1)
for i in range(M):
    a, b = map(int,(input().split()))
    graph[a].append(b)
    graph[b].append(a)
def recursion(x):
    visit[x] = 1
    for i in graph[x]:
        if visit[i] == 0:    
            recursion(i)
count = 0
for i in range(1,N+1):
    if visit[i] == 0:
        recursion(i)
        count += 1
print(count)
