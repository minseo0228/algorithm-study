from collections import deque
N,M = map(int,input().split())
numlist = [[] for _ in range(N+1)] 
for i in range(M):
    a,b = map(int,input().split())
    numlist[b].append(a)
def search(x):
    count = 0
    queue = deque()
    queue.append(x)
    while queue:
        a = queue.popleft()
        visit[a] = 1
        for i in numlist[a]:
            if visit[i] == 0:
                count += 1
                visit[i] = 1
                queue.append(i)
    return(count)

result = []
for i in range(1,N+1):
    visit = [0]*(N+1)
    result.append(search(i))

maxnum = max(result)
for i in range(len(result)):
    if result[i] == maxnum:
        print(i+1, end=' ')
