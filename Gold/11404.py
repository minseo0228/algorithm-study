from collections import deque
n = int(input())
m = int(input())
money = [[9999]*(m+1) for _ in range(n+1)]
visit = [0]*(m+1)
for i in range(m):
    a,b,c = map(int,input().split())
    bus[a].append([b,c])
for i in range(1,m+1):
    for j in range(1,m+1):
        