from collections import deque
N = int(input())
jang = [[]for _ in range(N+1)]
while True:
    a,b = map(int,(input().split()))
    if a == -1 and b == -1:
        break
    jang[a].append(b)
    jang[b].append(a)

def friend(x):
    visit = [0]*(N+1)
    queue = deque()
    queue.append(x)
    visit[x] = 1
    while queue:
        a = queue.popleft()
        for i in jang[a]:
            if visit[i] == 0:
                visit[i] = visit[a] + 1
                queue.append(i)
    a = max(visit)
    return(a)

result = []
for i in range(1,N+1):
    result.append(friend(i))


minnum = 1000
for i in result:
    minnum = min(minnum,i)

indexnum = []
for i in range(len(result)):
    if result[i] == minnum:
        indexnum.append(i+1)

print(minnum-1,len(indexnum))
for i in indexnum:
    print(i,end=" ")