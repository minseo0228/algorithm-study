from collections import deque
import sys
N,K = map(int,sys.stdin.readline().split())
queue = deque()
visit = [0]*(100001)
def bfs(v):
    queue.append(v)
    while queue:
        x = queue.popleft()
        if x < 0  or x > 100000:
            continue
        if x == K:
            print(visit[K])
            break
        for i in (x+1,x-1,x*2):
            if i < 0 or i > 100000 or visit[i]:
                continue
            visit[i] = visit[x] +1
            queue.append(i)     
bfs(N)