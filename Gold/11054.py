n = int(input())
num = list(map(int,input().split()))
dp = [0]*n
for i in range(n):
    start = num[i]
    for j in range(1,n+1):
        