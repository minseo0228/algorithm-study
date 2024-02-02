n, m = map(int,input().split())
tlist = set(input().split()[1:])
plist = []
a = 0

for i in range(m):
    flag = 0
    plist.append(set(input().split()[1:]))

for _ in range(m):
    for p in plist:
        if p & tlist:
            tlist = tlist.union(p)
# print(plist)
# print(tlist)
for p in plist:
    if p & tlist: #교집합 구하기
        continue
    a += 1

print(a)
