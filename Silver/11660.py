import sys

n,m = map(int, sys.stdin.readline().split())
numlist = []
for i in range(n):
    numlist.append(list(map(int, sys.stdin.readline().split())))
l = len(numlist[0])
# def calnum(x1,y1,x2,y2,numlist):
#     s = 0
#     for i in range(x1-1,x2):
#         for j in range(y1-1,y2):
#             s += numlist[j][i]
#     return s

ps = [[0]*(l+1) for _ in range(n+1)]
for i in range(0,l+1):
    for j in range(0,n+1):
        ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + numlist[i-1][j-1]
# print(ps)
for _ in range(m):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    print(ps[x2][y2] - ps[x2][y1-1] - ps[x1-1][y2] + ps[x1-1][y1-1]) 