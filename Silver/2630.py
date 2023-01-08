#분할정복으로 푸는 것이 좋다고 하는 군
#4분할해서 1이 그만큼 있으면 파란색 사각형
N = int(input())
graph = []
for i in range(N):
    list1 = list(input().split())
    graph.append(list1)

def divide(x,y,length): #4분할하고 처음에 들어온 색이 0인지 1인지 파악후 파랑인지 하양인지
    global blue, white
    check = 0
    color = graph[x][y]
    for i in range(x,x+length):
        for j in range(y,y+length):
            if graph[i][j] != color: #처음 첫번쨰 칸이랑 같지 않으면 다시 분할 ㄱ
                length2 = length//2
                divide(x,y,length2) 
                divide(x+length2,y,length2)
                divide(x,y+length2,length2)
                divide(x+length2,y+length2,length2)
                check = 1 #check를 해서 1이면 분할 했다는 의미니깐 white랑 blue증가 x
                return #함수의 실행을 끝맺음
    if check == 0:
        if color == '0':
            white += 1
        else:
            blue += 1
blue = 0   
white = 0
divide(0,0,N)
print(white)
print(blue)