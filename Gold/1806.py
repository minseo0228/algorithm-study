n, target = map(int,input().split())
numlist = list(map(int, input().split()))

# 누적합
# sumlist = [0]*len(n)
# sumlist[0]=numlist[0]
# for i in range(1,n):
#     sumlist[i] = numlist[i] + sumlist[i-1]

start = 0
end = 0
l = 1e9
s = numlist[0]
while True:
    if start > end:
        break
    # if end >= n:
    #     break
    # 총 합이 목표치보다 크거나 같으면 s보다 작아질때까지 빼본다. 
    if s >= target:
        l = min(l, end-start+1)
        s -= numlist[start]
        start += 1
    # 총 합이 작으면 end를 하나씩 더한다. 
    else:
        end += 1
        if end >= n:
            break
        s += numlist[end]
if l == 1e9:
    print(0)
else:
    print(l)
# #시간초과
# n,m = map(int,input().split())
# numlist = list(map(int, input().split()))
# dp = 1e9
# for i in range(len(numlist)):
#     s = 0
#     for j in range(i, len(numlist)):
#         s += numlist[j]
#         if s >= m:
#             dp = min(dp,j-i+1)
#             break
# if dp == 1e9:
#     print(0)
# else:
#     print(dp)
