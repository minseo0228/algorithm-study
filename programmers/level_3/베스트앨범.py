def solution(genres, plays):
    answer = []
    dict = {}
    for i in range(len(genres)):
        if genres[i] in dict:
            dict[genres[i]] += plays[i]
        else:
            dict[genres[i]] = plays[i]
    dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    music = []
    for i,z in dict:
        for j in range(len(genres)):
            if genres[j] == i:
                music.append([j,plays[j]])
        if len(music) == 1:
            answer.append(music[0][0])
            music = []
            continue
        else:
            music.sort(key=lambda x: x[1], reverse=True)
            for k in range(2):
                answer.append(music[k][0])
            music = []
    return answer