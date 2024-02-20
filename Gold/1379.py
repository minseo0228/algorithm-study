import heapq
n = int(input())
room = []
for _ in range(n):
    # 강의 번호, 시작시간, 끝나는 시간 
    room.append(list(map(int,input().split())))

# 끝나는 시간을 기준으로 정렬
room.sort(key=lambda x:x[1])

hq = []

# heapq.heappush(hq, [room[0][0], room[0][1], room[0][2]])
# 각 강의마다 어떤 강의실 번호인지
lecture = [0] * (n)

num = 0
for index, start_time, end_time in room:
    # 그 다음 시작 값이 작은 값은 pop한다. 
    # hq가 비어있으면 pop한다. -> 강의실 배정 
    # 강의 시작 시간이 더 크면 추가적인 강의실 배정할 필요 없다. -> pop
    if hq and hq[0][2] <= start_time:
        # print(lecture)
        lecture[index-1] = lecture[hq[0][0]]
        heapq.heappop(hq)
    else:
        # print(num)
        num += 1
        lecture[index-1] = num
    heapq.heappush(hq,[index,start_time,end_time])
    # print(hq)

print(num)
# # print(lecture[1:])
for i in lecture:
    print(i)
# print(lecture)
