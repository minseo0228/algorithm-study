from collections import deque
a, b = map(int,input().split())
q = deque()
flag = 0
q.append((a,0))
while q:
    number, time = q.popleft()
    if number == b:
        flag = 1
        print(time+1)
        break
    if number < b:
        x = str(number)+'1'
        q.append((int(x),time+1))
        q.append((number*2,time+1))
if flag == 0:
    print(-1)