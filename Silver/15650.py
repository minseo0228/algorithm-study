from itertools import combinations
n,m = map(int, input().split())
numlist = []
for i in range(1,n+1):
    numlist.append(i)
for j in list(combinations(numlist,m)):
    for k in j:
        print(k, end = ' ')
    print()