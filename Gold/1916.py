import heapq
# n = int(input())
# m = int(input())
# bus = [[] for _ in range(n+1)]
# for i in range(m):
#    s,e,p = map(int,input().split())
#    bus[s].append([e,p])
# # print(bus)
# start, end = map(int,input().split())
# dp = [1e9 for _ in range(n+1)]
# dp[start] = 0
# q = []
# heapq.heappush(q, [0,start])
# while q:
#    price, s = heapq.heappop(q)
#    if dp[s] < price:
#       continue
#    for e, p in bus[s]:
#       sumcost = price + p
#       if dp[end] <= sumcost:
#          continue
#       dp[end] = sumcost
#       heapq.heappush(q,[sumcost, end])

# print(dp[end])
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
        
start, end = map(int, input().split())
costs = [1e9 for _ in range(n+1)]
heap = []
costs[start] = 0
heapq.heappush(heap, [0, start])
    
while heap:
    cur_cost, cur_v = heapq.heappop(heap)
    if costs[cur_v] < cur_cost:
        continue
    for next_v, next_cost in graph[cur_v]:
        sum_cost = cur_cost + next_cost
        if sum_cost >= costs[next_v]:
            continue
        
        costs[next_v] = sum_cost
        heapq.heappush(heap, [sum_cost, next_v])
        
print(costs[end])