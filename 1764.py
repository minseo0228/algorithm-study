N,M = map(int,input().split())
set1 = set()
set2 = set()
for i in range(N):
    set1.add(input())
for i in range(M):
    set2.add(input())
set3 = list(set1 & set2)
print(len(set3))
set3.sort()
for i in range(len(set3)):
    print(set3[i])
