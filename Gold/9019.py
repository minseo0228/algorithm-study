from collections import deque
import sys
input = sys.stdin.readline
def L(a):
    num = a
    a = num%1000*10 + num//1000
    return(a)
     
def R(a):
    num = a
    a = num%10*1000 + num//10
    return(a)
for i in range(int(input())):
    first, second = map(int,input().split())
    visit = [0]*10000
    queue = deque()
    queue.append((first,''))
    while queue:
        n , op = queue.popleft()
        if n == second:
            print(op)
            break
        num = (n*2)%10000
        if visit[num] == 0:
            visit[num] = 1
            queue.append((num,op+'D'))
        num = (n-1)%10000
        if visit[num] == 0:
            visit[num] = 1
            queue.append((num,op+'S'))
        num = L(n)
        if visit[num] == 0:
            visit[num] = 1
            queue.append((num,op+'L'))
        num = R(n)
        if visit[num] == 0:
            visit[num] = 1
            queue.append((num,op+'R'))

    