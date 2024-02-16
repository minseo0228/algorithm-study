import heapq
n = int(input())
time = []
for _ in range(n):
    time.append(list(map(int,input().split())))

time.sort(key = lambda x:x[0])
hq = []
heapq.heappush(hq, time[0][1])
for i in range(1,n):
    if hq[0] <= time[i][0]:
        heapq.heappop(hq)
    heapq.heappush(hq, time[i][0])

print(len(hq))
