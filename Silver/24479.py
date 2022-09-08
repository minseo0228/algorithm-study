import sys
sys.setrecursionlimit(10 ** 6) 
n,m,r= map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
visted =[0]*(n+1)
count=1
def dfs(graph,v,visted):
    global count
    visted[v]=count
    for i in graph[v]:
        if visted[i]==0:
            count+=1
            dfs(graph,i,visted)
 
for i in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
 
for i in range(n+1):
    graph[i].sort()
 
dfs(graph,r,visted)

for i in range(1,n+1):
    print(visted[i])