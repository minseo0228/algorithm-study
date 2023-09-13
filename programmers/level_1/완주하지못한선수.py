def solution(participant, completion):
    dict = {}
    for i in participant:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for i in completion:
        if i in dict:
            if dict[i] == 1:
                del dict[i]
            else:
                dict[i] -= 1
    return list(dict.keys())[0]