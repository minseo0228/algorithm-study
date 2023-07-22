from collections import deque
#반시계 -1 시계 1
#2-6 index번호
#0 n극 1 s극
#1번 1 : 1점, 2번 1 : 2점, 3번 1 : 4점, 4번 1 : 8점

# a = 번호 , b =  방향 회전하는 것~~
def turnleft(a,b):
    if a >= 0:
        if graph[a][2] != graph[a+1][6]:
            turnleft(a-1,-b) 
            graph[a].rotate(b)

def turnright(a,b):
    if a <= 3:
        if  graph[a][6] != graph[a-1][2]:
            turnright(a+1,-b) 
            graph[a].rotate(b)


graph = []
for i in range(4):
    graph.append(deque(map(int,input())))

k = int(input())
for i in range(k):
    a,b= map(int,input().split())
    #왼편,오른편 확인 돌리기
    a -= 1
    turnleft(a-1,-b)
    turnright(a+1,-b)
    graph[a].rotate(b)

point = 0
for i in range(4):
    if graph[i][0] == 1:
        point += 2**i
print(point)