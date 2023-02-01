from collections import deque
num = int(input())
room = []
result = []
for i in range(num):
    a,b = map(int,input().split())
    room.append([a,b])
room.sort(key = lambda x:x[0])
room.sort(key = lambda x:x[1])#두번째 회의 끝나는 시간기준으로 정렬
#그래야 더 많은 회의를 잡을 수 있다!!

finish = room[0][1]
count = 1
for i in range(1,num):
    if room[i][0] >= finish:
        count += 1
        finish = room[i][1]
print(count)