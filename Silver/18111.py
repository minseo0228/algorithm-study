import sys
n,m,b = map(int, sys.stdin.readline().split())
graph =[]
time = 99999999
height = 0
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

maxblock = max(graph)
#블록 제거 2 블록 넣기 1
for i in range(257):
    t = 0
    use = 0
    take = 0
    for j in range(n):
        for k in range(m):
            #i보다 작은경우 블록 사용 + 1 -> b - 1
            if graph[j][k] < i:
                use += i-graph[j][k]
            #i보다 클 경우 블록 제거 + 2
            elif graph[j][k] > i:
                take += graph[j][k] - i
    if use > b + take:
        continue
    t = use + take*2
    if time >= t:
            height = i
            time = t

print(time,height)
