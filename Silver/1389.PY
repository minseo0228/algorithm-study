from collections import deque

n , m = map(int, input().split())
relation = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

def search_bacon(x):
    visit = [0]*(n+1)
    relations = [0]*(n+1)
    q = deque()
    q.append((x,0))
    visit[x] = 1
    while q:
        start, r = q.popleft()
        for i in relation[start]:
            if visit[i] == 0:
                visit[i] = 1
                q.append((i, r+1))
                relations[i] = r+1

    return relations


max_num = 1e9
for i in range(1,n+1):
    list1 = search_bacon(i)
    # print(list1)
    # s = sum(list1[1:i])+sum(list1[i+1:])
    s = sum(list1)
    if s < max_num:
        result = i
        max_num = s
print(result)
        
