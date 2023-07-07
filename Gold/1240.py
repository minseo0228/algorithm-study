from collections import deque
n,m = map(int,input().split())
graph = [[]for _ in range(n+1)]
for i in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

def bfs(x,y,node):
    visit = [0]*(n+1)
    q = deque()
    q.append((x,node))
    while q:
        x,node = q.popleft()
        if x == y:
            return(node)
        list1 = graph[x]
        for i in list1:
            a = i[0]
            if visit[a] == 0:
                visit[a] = 1
                q.append((a,node+i[1]))

for i in range(m):
    node = 0
    x,y = map(int,input().split())
    print(bfs(x,y,node))
    
