def solution(survey, choices):
    answer = ''
    mbti = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(survey)):
        a = survey[i]
        if choices[i] >= 4:
            a = a[1]
            mbti[a] += choices[i] - 4
        else:
            a = a[0]
            mbti[a] += 4 - choices[i]
    print(mbti)
    if mbti['R']>= mbti['T']:
        answer = answer + 'R'
    else:
        answer = answer + 'T'
    if mbti['C']>= mbti['F']:
        answer = answer + 'C'
    else:
        answer = answer + 'F'
    if mbti['J']>= mbti['M']:
        answer = answer + 'J'
    else:
        answer = answer + 'M'
    if mbti['A']>= mbti['N']:
        answer = answer + 'A'
    else:
        answer = answer + 'N'
    print(answer)
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]	
choices = 	[5, 3, 2, 7, 5]
solution(survey, choices)