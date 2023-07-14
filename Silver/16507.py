r,c,q = map(int,input().split())

map1 = [list(map(int,input().split())) for _ in range(r)]

graph = [[0]*(c+1) for _ in range(r+1)]

for i in range(1,r+1):
    for j in range(1,c+1):
        graph[i][j] = map1[i-1][j-1] + graph[i-1][j] + graph[i][j-1] - graph[i-1][j-1]

for _ in range(q):          
    r1,c1,r2,c2 = map(int,input().split())
    count = (c2-c1+1)*(r2-r1+1)
    result = graph[r2][c2] -graph[r2][c1-1] -graph[r1-1][c2] + graph[r1-1][c1-1]
    print(result//count)