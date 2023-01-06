n,r,c = map(int,(input().split()))
count = 0
length = (2**n)//2 #전체 길이의 반 4분면을 나누기 위해서!
while(n>0):
    n -= 1
    length = (2**n) #전체 길이의 반 4분면을 나누기 위해서!
    if (c<length) and (r<length): #2사분면일때는 안움직여도 됨
        continue
    elif (c>=length) and (r<length): #1사분면일때 2사분면으로 R,C를 이동시켜주고 그만큼 방문해야하니깐 그만큼 COUNT에 더해줘
        count += (length**2)
        c -= length
    elif (c<length) and (r>=length): #3사분면일때도 마찬가지
        count += (length**2)*2
        r -= length
    else: #4분면일때
        count += (length**2)*3
        c -= length
        r -= length
print(count)