N, new, P = map(int,input().split())
score = []
if N != 0:
    score = list(map(int,input().split()))
for i in range(P):
    if not score:
        print(1)
        break
    if new > score[i]:
        print(i+1)
        break
    if score[i] == new:
        if i == P-1:
            print(-1)
            break
        else:
            if score[i] == score[i+1]:
                continue
            print(i+1)
            break