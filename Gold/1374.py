import heapq
n = int(input())
room = []
for i in range(n):
    room.append(list(map(int,input().split())))

room.sort(key=lambda x:x[1])
hq = []

heapq.heappush(hq, room[0][2])
for i in range(1,n):
    if room[i][1] >= hq[0]:
        heapq.heappop(hq)
    heapq.heappush(hq,room[i][2])

print(len(hq))