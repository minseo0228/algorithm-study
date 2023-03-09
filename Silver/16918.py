# R,C,N = map(int,input().split())
# graph = []
# time = [[0]*C for _ in range(R)]
# for i in range(R):
#     graph.append(list(input()))

# def time1(graph,time): #아무일도 안일어남-> 시간만 +1
#     for i in range(R):
#         for j in range(C):
#             if graph[i][j] == 'O':
#                 time[i][j] += 1
            
# def time2(graph,time): #설치되어 있지 않으면 -> 폭탄설치
#     for i in range(R):
#         for j in range(C):
#             if graph[i][j] == 'O':
#                 time[i][j] += 1
#             elif graph[i][j] == '.':
#                 graph[i][j] = 'O'
#                 time[i][j] += 1

# movex = [1,0,-1,0]
# movey = [0,1,0,-1]
# def time3(graph,time): #3초된 폭탄 폭발
#     for i in range(R):
#         for j in range(C):
#             if graph[i][j] == 'O':
#                 time[i][j] += 1
#                 if time[i][j] >= 3:
#                     graph[i][j] = '.'
#                     time[i][j] = 0
#                     for k in range(4):
#                         x = i + movex[k]
#                         y = j + movey[k]
#                         if x < 0 or y < 0 or x >= R or y >= C:
#                             continue
#                         if graph[x][y] == 'O':
#                             time[x][y] = 0
#                             graph[x][y] = '.'

# time1(graph,time)
# for i in range(2,N+1):
#     # print(i)
#     if i%2 == 0:
#         time2(graph,time)
#     else:
#         time3(graph,time)
#     # print()
#     # pprint(graph)

# for i in range(R):
#     for j in range(C):
#         print(graph[i][j], end ='')
#     print()
from collections import deque
R,C,N = map(int,input().split())
graph = []

for i in range(R):
    graph.append(list(input()))

def time1():
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'O':
                bomb.append((i,j))

def time2():
    for i in range(R):
        for j in range(C):
            if graph[i][j] == '.':
                graph[i][j] = 'O'

movex = [1,0,-1,0]
movey = [0,1,0,-1]

def time3():
    while bomb:
        x,y = bomb.pop()
        for i in range(4):
            nx = x + movex[i]
            ny = y + movey[i]
            if 0<=nx<R and 0<=ny<C:
                if graph[nx][ny] == 'O':
                    graph[nx][ny] = '.'

N -= 1

while True:
    # bomb = []
    bomb = deque()
    time1()
    time2()
    N-=1
    if N == 0:
        break
    time3()
    N-=1

for i in range(R):
    for j in range(C):
        print(graph[i][j], end ='')
    print()