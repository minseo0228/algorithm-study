def solution(n, lost, reserve):
    stu = [1]*(n+1) #다 가지고 있다고 가정
    for i in lost:
        stu[i] -= 1
    for i in reserve:
        stu[i] += 1
    
    for i in range(1,len(stu)-1):
        if stu[i] >= 2:
            if stu[i-1] == 0:
                stu[i-1] += 1
                stu[i] -= 1 
            elif stu[i+1] == 0:
                stu[i+1] += 1
                stu[i] -= 1
    if stu[len(stu)-1] >= 2:
        if stu[len(stu)-2] == 0:
            stu[len(stu)-2] += 1
            stu[len(stu)-1] -= 1
    count = -1
    for i in stu:
        if i >= 1:
            count += 1
    return count
