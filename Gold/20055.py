from collections import deque
N,K = map(int,input().split())
belt = deque(map(int,input().split()))
robot = deque([0]*N) #N까지만 로봇이 존재해

result = 0
while True:
    #단계 += 1
    result += 1
    #1.로봇 회전
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    #2.가장 먼저 올라간 로봇부터 이동할 수 있으면 이동
    for i in range(N-2,-1,-1):
        if robot[i] == 1:
            if belt[i+1] >= 1 and robot[i+1] == 0:
                robot[i+1] = 1
                robot[i] = 0
                belt[i+1] -= 1
    robot[-1] = 0
    #3.로봇 올리기
    if robot[0] == 0 and belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1
    #4.내구도 확인 및 종료
    if belt.count(0) >= K:
        break
print(result)