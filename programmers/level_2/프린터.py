def solution(priorities, location):
    answer = 0
    pq = []
    for i in range(len(priorities)):
        pq.append([i,priorities[i]]) # 이렇게 안하고 enumerate 함수도 있더라~
    while True:
        x = pq.pop(0)
        if any(x[1] < i[1]  for i in pq): ## any를 사용해서 하나라도 큰게 있으면 패스 할 수 있게 해줌
            pq.append(x)
        else:
            answer += 1
            if x[0] == location:
                return  answer