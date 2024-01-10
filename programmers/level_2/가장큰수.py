# from itertools import permutations
# def solution(numbers):
#     answer = ''
#     maxnum = 0
#     plist = permutations(numbers,len(numbers))
#     for i in plist:
#         num = ''
#         for j in i:
#             num = num + str(j)
#         num = int(num)
#         maxnum = max(num, maxnum)
#     answer = str(maxnum)
               
#     return answer
# 시간초과

## 2차 시도
# def solution(numbers):
#     answer = ''
#     maxnum = 0
#     num = ''
#     numlist = [ [] for _ in range(len(numbers))]
#     # 같은 자릿수를 만들어 비교!
#     for i in range(len(numbers)):
#         num = ''
#         if len(str(numbers[i])) == 1:
#             num = str(numbers[i]) + '00'
#             numlist[i] = int(num)
#         elif len(str(numbers[i])) == 2:
#             num = str(numbers[i]) + '0'
#             numlist[i] = int(num)
#         else:
#             numlist[i] = numbers[i]

#     sorted_index = sorted(range(len(numlist)), key=lambda i: numlist[i], reverse=True)
#     numlist = [numlist[i] for i in sorted_index]
#     numbers = [numbers[i] for i in sorted_index]
#     print(numbers)
#     print(numlist)
#     for i in numbers:
#         answer = answer + str(i)
#     answer = int(answer)
               
#     return answer

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))  # 숫자 배열을 문자열 배열로 변환
    numbers.sort(key=lambda x: x * 3, reverse=True)  # 각 문자열을 3번 반복하여 비교하여 정렬

    answer = str(int(''.join(numbers)))  # 숫자를 문자열로 합쳐서 정수로 변환한 후 다시 문자열로 변환

    return answer
