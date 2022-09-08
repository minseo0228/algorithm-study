# 가장 짧은 길이 1을 start, 나무 중 가장 긴 길이를 end로 
# while 문 
# mid 를 start와 end 중간에 두고 모든 값에서 mid를 빼 총 어느 정도
# 길이의 벌목된 나무가 나오나 본다. 
# 벌목 나무가 목표치 이상이면 mid+1을 start로 두고 다시 while문
# 벌목 나무가 목표치 이하이면 mid-1을 end로 두고 다시 while문
# start와 end가 같아지면 결과값 출력

a,b = map(int,(input().split()))
bst = list(map(int,(input().split())))
start = 1
bst.sort()
end = bst[a-1]
while True:
    mid = (start+end)//2
    na = 0
    for i in bst:
        if i >= mid:
            na += i - mid
    if na >= b:
        start = mid + 1
    else:
        end = mid - 1
    if start > end:
        break
print(end) 
