from itertools import product
N,M = map(int,input().split())
num = list(input().split())
num.sort()
numlist = list(product(num,repeat=M))
numlist = sorted(list(set(numlist)))
for i in numlist:
    print(''.join(i))

from itertools import product

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
cmb = list(product(a, repeat=m))
ans = []

for c in cmb:
    ans.append(c)

ans = sorted(list(set(ans))) 

for c in ans:
    for i in c:
        print(i, end=' ')
    print()