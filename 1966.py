from collections import deque
N = int(input())
for i in range(N):
    queue = deque()
    num,q = map(int,input().split())
    list1 = []
    list1 = list(map(int, input().split()))
    index = max(list1)
    for i in range(len(list1)):
        

