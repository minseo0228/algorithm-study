import sys
input = sys.stdin.readline
x, y = map(int,(input().split()))
numlist = list(map(int, input().split()))
sumlist = [0]
temp = 0
for i in numlist:
    temp += i
    sumlist.append(temp)
for _ in range(y):
    a,b = map(int,(input().split()))
    sum =  sumlist[b] - sumlist[a-1]
    print(sum)
