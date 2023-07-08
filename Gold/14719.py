a,b = map(int, input().split())
num = list(map(int,input().split()))
water = 0
for i in range(1,b-1):
    left = max(num[:i]) #왼쪽에서 가장 큰 수
    right = max(num[i+1:]) #오른쪽에서 가장 큰 수
    minblock = min(left, right)
    if num[i] < minblock:
        water += minblock-num[i]
print(water)