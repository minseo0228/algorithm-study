from collections import deque
N = int(input())
graph = []
for i in range(N):
    graph.append(list(input()))
#아 미친 이거 쉬운 문제였자나...
#처음에 그래프를 이해를 잘못해서 N = 3인경우 9명이라고 생각하고 풀어버렸다.
#근데 이 문제는 그냥 대각선 반으로 접었을때 똑같은 문제이고 
#한줄씩 파악만 해주면 되는 부분!!

result = []
def bfs(x):
    visit = [0]*N
    count = 0
    queue = deque()
    queue.append((x,0))
    visit[x] = 1
    while queue:
        x,c = queue.popleft()
        if c >= 2: #2보다 멀어지면 친구가 될 수 없아..
            continue
        for i in range(N):
            if visit[i] == 0 and graph[i][x] == 'Y':
                visit[i] = 1
                queue.append((i,c+1))
                count += 1
    result.append(count)

for i in range(N):
    bfs(i)
print(max(result))      