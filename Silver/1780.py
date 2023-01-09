N = int(input())
graph = []
for i in range(N):
    list1 = list(map(int,input().split()))
    graph.append(list1)

def check(x,y,length):
    chk = 0
    global zero, minus, plus
    color = graph[x][y]
    for i in range(x,x+length):
        for j in range(y,y+length):
            if graph[i][j] != color:
                length = length//3
                check(x,y,length)
                check(x+length,y,length)
                check(x+(2*length),y,length)
                check(x,y+length,length)
                check(x+length,y+length,length)
                check(x+(2*length),y+length,length)
                check(x,y+(2*length),length)
                check(x+length,y+(2*length),length)
                check(x+(2*length),y+(2*length),length)
                chk = 1
                return
    if chk == 0:
        if color == 0:
            zero += 1
        elif color == 1:
            plus += 1
        else:
            minus += 1


minus = 0
zero = 0
plus = 0
check(0,0,N)
print(minus)
print(zero)
print(plus)


