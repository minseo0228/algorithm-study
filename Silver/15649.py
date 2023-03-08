from itertools import permutations
N,M = map(int,input().split())
num = []
for i in range(1,N+1):
    num.append(i)
numlist = []
for i in permutations(num,M):
    numlist.append(i)
for i in range(len(numlist)):
    a = numlist[i]
    for j in range(len(a)):
        print(a[j], end= ' ')
    print()