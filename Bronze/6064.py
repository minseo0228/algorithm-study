T = int(input())
for _ in range(T):
    M, N , x, y = map(int, input().split())
    countx = 0
    county = 0
    count = 0
    while (1):
        while (county == N):
            county = county + 1
            count = count + 1
