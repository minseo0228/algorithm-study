from collections import deque
n,m,x = map(int, input().split())

road = [[] for _ in range(n+1)]
for i in range(m):
    s,e,t = map(int,input().split())
    road[s].append((e,t))

def find_time(s,dest):
    dp = [1e9 for _ in range(n+1)]
    q = deque()
    q.append((s, 0))
    while q:
        start, time  = q.popleft()
        # if start == dest:
        #     break
        for end,t in road[start]:
            ft = time + t
            if dp[end] > ft:
                dp[end] = ft
                q.append((end, ft))
    return(dp[dest])


answer = [0 for _ in range(n+1)]
for i in range(1,n+1):
    # for end, time in road[i]:
    #     # answer[i].append(find_time(end,time))
    #     print(find_time(end,time))
    if i == x:
        continue
    y = find_time(i,x)
    z = find_time(x,i)
    answer[i] = y+z
    
print(max(answer))

