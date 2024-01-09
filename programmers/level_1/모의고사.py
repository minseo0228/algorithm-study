def countdef(answers,answerslist):
    count = 0
    for i in range(len(answers)):
        if answers[i] == answerslist[i]:
            count += 1 
    return count

def solution(answers):
    answer = []
    no1 = [1,2,3,4,5]*2000
    no2 = [2,1,2,3,2,4,2,5]*2000
    no3 = [3,3,1,1,2,2,4,4,5,5]*2000
    x = countdef(answers,no1)
    y = countdef(answers,no2)
    z = countdef(answers,no3)
    maxnum = max(x,y,z)
    if maxnum == x:
        answer.append(1)
    if maxnum == y:
        answer.append(2)
    if maxnum == z:
        answer.append(3)
    return answer
