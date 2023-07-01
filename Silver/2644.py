from collections import deque
N = int(input())
a,b = map(int,input().split())
m = int(input())
relation = [[] for _ in range(N+1)]
for i in range(m):
    x,y = map(int,input().split())
    relation[x].append(y)
    relation[y].append(x)
print(relation)

def bfs():
    bridge = 0
    q = deque()
    q.append((a,b,bridge))
    while q:
        sibiling = []
        start,end,bridge = q.popleft()
        sibiling = relation[start]
        if end in sibiling:
            bridge += 1
            break
        elif len(sibiling) == 0:
            bridge = -1
            break
        else:
            for i in sibiling:
                bridge += 1
                q.append((i,end,bridge))
    print(bridge)

bfs()

