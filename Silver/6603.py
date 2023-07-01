from itertools import combinations
while(True):
    numlist = list(map(int,input().split()))
    if len(numlist)== 1 and numlist[0] == 0:
        break
    numlist.pop(0)
    numlist.sort()
    rotto = list(combinations(numlist,6))
    for i in rotto:
        print(*i)
    print()