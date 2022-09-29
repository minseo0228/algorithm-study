from collections import deque
x = int(input())
count = 0
visit = [0]*1000000
def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    while deque:
        num, count = queue.popleft()
        if num == 1:
            print(count)
            break
        if num % 3 == 0:
            temp = num // 3
            if visit[temp] == 0:
                visit[temp] = 1
                queue.append((temp, count+1))
        if num % 2 == 0:
            temp = num // 2 
            if visit[temp] == 0:
                visit[temp] = 1
                queue.append((temp, count+1))
        temp = num - 1
        if visit[temp] == 0:
            visit[temp] = 1
            queue.append((temp, count+1))
bfs(x,0)