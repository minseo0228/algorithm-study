from collections import deque
N = int(input())
a,b = map(int,input().split())
m = int(input())
relation = [[] for _ in range(N+1)]
for i in range(m):
    x,y = map(int,input().split())
    relation[x].append(y)
    relation[y].append(x)

def bfs(x,y):
    visit = [0 for _ in range(N+1)]
    bridge = 0
    q = deque()
    q.append(x)
    end = y
    visit[x] = 1
    flag = 0
    while q:
        start = q.popleft()
        for i in relation[start]:
            if visit[i] == 0:
                if i == end:
                    flag = 1
                    break
                visit[i] = visit[start] + 1
                q.append(i)
        # bridge += 1
        if flag == 1:
            break
    if flag == 0:
        print(-1)
    else:
        print(visit[start])

bfs(a,b)
