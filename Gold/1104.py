from collections import deque
n = int(input())
m = int(input())
bus = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    bus[a].append((b,c))


def price(i):
    dp = [1e9 for _ in range(n+1)]
    q = deque()
    q.append((i,0))
    while q:
        start, cost = q.popleft()
        for dest, n_cost in bus[start]:
            sum_cost = n_cost +  cost
            if dp[dest] > sum_cost:
                dp[dest] = sum_cost
                q.append((dest,sum_cost))
        # print(dp)
    return dp

result = [[0 for _ in range(n)] for _ in range(n)]

for i in range(1,n+1):
    r = price(i)
    for j in range(1,n+1):
        if i == j:
            result[i-1][j-1] = 0
            continue
        if r[j] == 1e9:
            continue
        else:
            result[i-1][j-1] = r[j]

for i in range(n):
    for j in range(n):
        print(result[i][j], end = ' ')
    print(" ")
