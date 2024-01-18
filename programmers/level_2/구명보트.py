def solution(people, limit):
    answer = 0
    #무거운 사람 먼저 
    people.sort(reverse = True)
    left = 0
    right = len(people) -1 
    while True:
        if left > right:
            break
        if people[left] + people[right] <= limit:
            right -= 1
        left += 1            
        answer += 1
    return answer