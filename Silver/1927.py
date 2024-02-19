import heapq
import sys
input=sys.stdin.readline
hq = []
n = int(input())
for i in range(n):
    x = int(input())
    if x == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq,x)