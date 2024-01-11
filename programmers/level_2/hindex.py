def solution(citations):

    n = max(citations)
    citations.sort(reverse = True)
    for i in range(n,0,-1):
        num = 0
        for j in citations:
            if j >= i:
                num += 1
        if num >= i:
            return i
    return 0