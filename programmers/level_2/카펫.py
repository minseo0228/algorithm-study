def solution(brown, yellow):
    answer = []
    m = []
    for i in range(1,yellow//2+1):
        if yellow % i == 0:
            print(i,yellow//i)
            m.append([i,yellow//i])
    if yellow == 1:
        if brown == 8:
            return([3,3])
    for i in m:
        x = i[0]
        y = i[1]
        if x*2+y*2+4 == brown:
            answer = [max(x+2,y+2),min(x+2,y+2)]
            return answer

    return answer