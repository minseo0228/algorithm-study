def solution(food):
    answer = ''
    for i in range(1,len(food)):
        if food[i] % 2 == 1:
            a = food[i] - 1
            food[i] = a 
        startpoint = len(answer)//2
        if startpoint == 0:
            for j in range(food[i]):
                num = i
                answer = answer + str(num)
        else:
            for j in range(food[i]):
                num = i
                answer = answer[0:startpoint] + str(num) + answer[startpoint:]
    startpoint = len(answer)//2
    answer = answer[0:startpoint] + '0' + answer[startpoint:]
    return answer

food = [1,3,4,6]
print(solution(food))
