#
from itertools import combinations
L,C = map(int,input().split())
word = list(input().split())
word.sort()
password = combinations(word,L)
def check(pw):
    EW = ['a','e','i','o','u']
    check = 0
    for i in range(5):
        if EW[i] in pw:
            check += 1
    if check == 0:
        return False
    else:
        return(check)

# def check2(pw):
#     for i in range(L-1):
#         if ord(pw[i+1])-ord(pw[i]) <= 0:
#             return False
#     return True

result = []
for i in password:
    a = check(i)
    # b = check2(i)
    # if a != False and b == True:
    if a != False:
        if L-a >= 2:
            i = list(i)
            print(''.join(i))