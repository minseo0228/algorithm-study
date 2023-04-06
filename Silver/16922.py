from itertools import combinations_with_replacement
from itertools import product
N = int(input())
visit = [0]*(50*N+1)
rome = [1,5,10,50]
a = combinations_with_replacement(rome,N)
b = product(rome,repeat=N)
count = 0
for i in a:
    i = list(i)
    summ = sum(i)
    if visit[summ] == 0:
        count += 1
    visit[summ] = 1
print(count)