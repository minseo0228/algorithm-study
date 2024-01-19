# 이거 pop써도 시간초과 나더라
def solution(number, k):
    maxn = 0
    answer = ''
    n = len(number)
    start = 0
    while True:
        if k <= 0 or start >= len(number)-1:
            break
        if number[start] < number[start+1]:
            number = number[:start] + number[start+1:]
            k -= 1
            if start > 0:
                start -= 2
            else:
                start -= 1
        start += 1
    
    if k>0:
        number = number[:len(number)-k]

    return number