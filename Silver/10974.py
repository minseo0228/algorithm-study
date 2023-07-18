from itertools import permutations
n = int(input())
numlist = [i for i in range(1,n+1)]
result = list(permutations(numlist,n))
for i in result:
    for j in i:
        print(j,end=' ')
    print()