from collections import deque
q = deque()
n,m = map(int,input().split())
# 진입
rule = [0 for _ in range(n+1)]
h = [[] for _ in range(n+1)]
for i in range(m):
    x,y = map(int,input().split())
    rule[y] += 1
    h[x].append(y)
# print(rule)
# print(h)
for i in range(1,n+1):
    if rule[i] == 0:
        q.append(i)
result = []
# print(rule)
while q:
    x = q.popleft()
    result.append(x)
    for i in h[x]:
        rule[i] -= 1
        if rule[i] == 0:
            q.append(i)

for i in result:
    print(i, end= ' ')

        

