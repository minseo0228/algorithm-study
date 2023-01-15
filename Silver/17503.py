import heapq
N,M,K = map(int,input().split())
beer = []
hq = []
for i in range(K):
    beer.append(list(map(int,input().split())))
beer.sort(key = lambda x:(x[1])) #도수 레벨을 기준으로 정렬
# beer = 선호도, 도수레벨 -> 도수가 낮은 순서로 정렬
# print(beer)
find = False
now_alchol = 0
like = 0
for i in range(K):
    #힙에다가 선호도를 넣어줘
    heapq.heappush(hq,beer[i][0])
    print(hq)
    #힙에다가 넣은 선호도를 like에 더해
    like += beer[i][0]
    print(like)
    now_alchol = beer[i][1]
    #그 선호도가 now_alchol이 그 도수 레벨이 되는거지 
    print(now_alchol)
    if len(hq) == N: #힙큐에 있는 것들이 날짜와 같으면
        if like >= M: #그리고 선호도는 M보다 크거나 같으면
            find = True
            print(now_alchol) #경과 출력
            break
        else: #만약 갯수가 아니라면 가장 작은 항목을 반환
            like -= heapq.heappop(hq)
            #선호도도 빼줘
if not find:
    print(-1)