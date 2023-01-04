from collections import Counter
def solution(id_list, report, k):
    print(report)
    report = list(set(report))
    print(report)
    # dict = {}
    # for i in report:
    #     a,b = i.split()
    #     if b in dict.keys():
    #         key = dict[b] 
    #         value = []
    #         value.append(key)
    #         value.append(a)
    #         dict[b] = value
    #     else:
    #         dict[b] = a
    # dict1 = {}
    # for i in id_list:
    #     dict1[i] = 0
    # answer = [0 for _ in range(len(id_list))]
    # for i in dict.keys():
    #     if (isinstance(dict[i],list)==True):
    #         a = dict[i]
    #         if len(a) >= k:
    #             for j in range(len(a)):
    #                 if a[j] in dict1.keys():
    #                     y = dict1[a[j]] 
    #                     dict1[a[j]] = y + 1
    # j = 0
    # for i in dict1.values():
    #     answer[j] = i
    #     j += 1
    # print(answer)
    return answer

report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
id_list = ["muzi", "frodo", "apeach", "neo"]
k = 2
solution(id_list,report,k)

# from collections import Counter
# def solution(id_list, report, k):
#     temp=[]
#     temp2=[]
#     report=list(set(report))
#     for i in range(0,len(report)):
#         a=report[i].split(' ')
#         temp2.append(a)
#         temp.append(a[1])

#     dic={i:0 for i in id_list}    
#     counter=Counter(temp)

#     for j in counter.keys():
#         if counter[j]>=k:
#             for i in range(0,len(temp2)):
#                 if temp2[i][1]==j:
#                     dic[temp2[i][0]]+=1


#     return (list(dic.values()))
