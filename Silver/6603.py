from itertools import combinations
while(True):
    numlist = list(map(int,input().split()))
    if len(numlist)== 1 and numlist[0] == 0:
        break
    if 0 in numlist:
        numlist.remove(0)
    numlist = set(numlist)
    numlist = list(numlist)
    numlist.sort()
    rotto = list(combinations(numlist,6))
    for i in rotto:
        print(*i)
    print()