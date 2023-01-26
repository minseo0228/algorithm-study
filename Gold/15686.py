#아직 못품
from itertools import combinations
N,M = map(int,input().split())
graph = []

chicken = []
house = []
#치킨집의 위치를 찾아서 인덱스를 적어놓자.   
for i in range(N):
    list1 = list(map(int,input().split()))
    if 1 in list1 or 2 in list1:
        for j in range(len(list1)):
            if list1[j] == 1:
                house.append((i,j))
            elif list1[j] == 2:
                chicken.append((i,j))
    graph.append(list1)

# total = 9999
# for home in house:
#     home = list(home)
#     hx = home[0]
#     hy = home[1]
#     result = 0
#     for chick in combinations(chicken,M):
#         chick = list(chick)
#         dist = 9999
#         for j in range(M):
#             a = chick[j]
#             cx = a[0]
#             cy = a[1]
#             dist = min(dist,abs(hx-cx)+abs(hy-cy))
#         result += dist
#     total = min(total,result)
# print(total)

total = 9999
for chick in combinations(chicken,M):
    chick = list(chick)
    result = 0
    for home in house:
        home = list(home)
        hx = home[0]
        hy = home[1]
        dist = 9999
        for j in range(M):
            a = chick[j]
            cx = a[0]
            cy = a[1]
            dist = min(dist,abs(hx-cx)+abs(hy-cy))
        result += dist
    total = min(total,result)
print(total)