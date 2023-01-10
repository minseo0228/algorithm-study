N, K = map(int,input().split())
money = []
for i in range(N):
    money.append(int(input()))

count = 0
mon = K
for i in range(len(money)):
    x = money[len(money)-i-1]
    while mon//x > 0:
        mon -= x
        count += 1
print(count)