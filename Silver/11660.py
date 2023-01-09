import sys
N, M = map(int, sys.stdin.readline().strip().split())

graph = []
for _ in range(N):
    list1 = list(map(int,sys.stdin.readline().strip().split()))
    graph.append(list1)

def calsum(x,y,nx,ny):
    sum = 0
    for i in range(x,nx+1):
        for j in range(y,ny+1):
            sum += graph[i-1][j-1]
    return(sum)

for i in range(M):
    x,y,nx,ny = map(int,input().split())
    if x == nx and y == ny:
        print(graph[x-1][y-1])
    else:
        print(calsum(x,y,nx,ny))
