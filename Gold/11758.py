p1x,p1y = map(int,input().split())
p2x,p2y = map(int,input().split())
p3x,p3y = map(int,input().split())

#외적>0 -> 반시계
v = (p2x-p1x)*(p3y-p2y) - (p3x-p2x)*(p2y-p1y)
if v > 0:
    print(1)
elif v == 0:
    print(0)
else:
    print(-1)

# 직선 기울기 -> 모든 기울기가 값이 같은 경우 
# a1 = (p2y-p1y)/(p2x-p1y)
# a2 = (p3y-p2y)/(p3x-p2x)
# if a1 == a2:
#     print(0)
# else: #시계파악
#     a = (p2y-p1y)*(p3x-p2x) - (p3y-p2y)*(p2x-p1y)
#     if a > 0:
#         print(-1)
#     else:
#         print(1)
