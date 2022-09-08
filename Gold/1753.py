import heapq

V,E = map(int,input().split())
K = int(input())
INF = 100000000000
# 간선 간의 가중치를 나타내는 테이블
dp = [INF] * (V+1)
heap = []
graph = [[] for _ in range(V + 1)]

def Dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap,(0, start))

    while heap:
        dist, now = heapq.heappop(heap)
        if dp[now] < dist:
            continue
        for ndist, next in graph[now]:
            # ndist = 현재 위치의 가중치 dist + 다음 정점까지 가중치 ndist = 다음 노드까지 가중치 nextdist
            nextdist = ndist + dist
            if nextdist < dp[next]:
                dp[next] = nextdist
                # 다음 점 까지의 가중치와 정보를 튜플로 묶어 최소힙에 삽입
                heapq.heappush(heap,(nextdist, next))

for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((w,v))

Dijkstra(K)
for i in range(1, V+1):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])