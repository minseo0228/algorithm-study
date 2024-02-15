import heapq
n = int(input())
room = []
for i in range(n):
    room.append(list(map(int,input().split())))

# room에 시작점을 기준으로 sorting  
room.sort(key=lambda x:x[0])
# room.sort(key=lambda x:x[1])

hq = []
# hq에 처음 끝나는 시간 넣기
heapq.heappush(hq, room[0][1])

for i in range(1,n):
    # room 시작 시간이 끝나는 시간보다 크면 pop
    if room[i][0] >= hq[0]:
        # heap에서 가장 작은 원소를 pop
        heapq.heappop(hq)
    heapq.heappush(hq,room[i][1])

print(len(hq))
