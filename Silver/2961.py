from itertools import combinations
n = int(input())
food = []
for i in range(n):
    food.append(list(map(int,input().split())))

result = 99999999999
combilist = []
for j in range(1,n+1):
    combilist.append(combinations(food,j))
for j in combilist:
    for k in j:
        s = 1
        b = 0
        for i in k:
            s *= i[0]
            b += i[1]
        result = min(result,abs(s-b))

print(result)