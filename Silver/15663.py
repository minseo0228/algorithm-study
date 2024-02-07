from itertools import permutations
n,m = map(int,input().split())
numlist = list(map(int,input().split()))
list1 = []
for i in permutations(numlist,m):
    list1.append(i)
list1 = set(list1)
list1 = list(list1)
list1.sort()
for j in list1:
    for k in j:
        print(k, end = ' ')
    print()