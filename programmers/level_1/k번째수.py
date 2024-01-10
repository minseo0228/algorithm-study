def solution(array, commands):
    answer = []
    for x in commands:
        i = x[0]
        j = x[1]
        k = x[2]
        newarray = array[i-1:j]
        print(newarray)
        newarray.sort()
        answer.append(newarray[k-1])
    
    return answer