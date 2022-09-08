a,b = map(int,(input().split()))
maze = []
for i in range(a):
    maze.append(list(map(int,input())))
x=0
y=0
visited = [[0]*b for _ in range(a)]
movex = [1,0,-1,0]
movey = [0,1,0,-1]
from collections import deque
def bfs(x,y):
    count = 0
    queue = deque()
    queue.append((x,y))
    visited[0][0] = 0
    while queue:
        x,y = queue.popleft()
        visited[x][y] = 1
        print(x,y)
        if x ==a-1 and y==b-1:
            break
        for i in range(4):
         x1 = x + movex[i]
         y1 = y + movey[i]
         if (x1 >=a or y1>=b or x1<0 or y1<0):
            continue
         if maze[x1][y1] == 0:
            continue
         if visited[x1][y1] == 0:
            count += 1
            queue.append((x1,y1))
            visited[x1][y1] = 1
            print(count)
    return count
print(bfs(0,0))

