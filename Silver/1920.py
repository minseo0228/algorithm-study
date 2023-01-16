import sys
n = int(sys.stdin.readline())
numlist = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
numlist.sort()
def binary_search(x):
    check = 0
    start = 0
    end = n-1
    while(start <= end):
        mid = (start + end)//2
        if x < numlist[mid]:
            end = mid - 1
        elif x == numlist[mid]:
            check = 1
            break
        else:
            start = mid + 1
    print(check)
for i in range(m):
    binary_search(num[i])

    