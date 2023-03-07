N = int(input())
check = []
checkpoint = []
dist = []
for i in range(N):
    a,b = map(int,input().split())
    check.append([a,b])
d = 0
for j in range(len(check)-1):
    x = abs(check[j+1][0] - check[j][0])
    y = abs(check[j+1][1] - check[j][1])
    dist.append(x + y)
    d += (x+y)
dist2 = []
for i in range(1,N-1):
    x = abs(check[i+1][0] - check[i-1][0])
    y = abs(check[i+1][1] - check[i-1][1])
    dist2.append(x + y)
print(dist)
print(dist2)
minnum = 100000
for i in range(len(dist2)):
    minnum  = min(dist2[i] + d - dist[i] - dist[i+1], minnum)
print(minnum)

