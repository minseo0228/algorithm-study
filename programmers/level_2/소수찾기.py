from itertools import permutations
def check(n):
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1
def solution(numbers):
    answer = 0
    nlist = list(numbers)
    numlist = []
    for i in range(1,len(nlist)+1):
        numlist += (permutations(nlist,i))
    final = []
    for i in numlist:
        n = int(''.join(i))
        if n in final:
            continue
        if n != 1 and check(n) == 1 and n != 0:
            answer += 1
        final.append(n)
    return answer
