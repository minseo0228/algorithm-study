N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))
num.sort(reverse=True)

flag = 1
for i in range(N-2):
    if num[i] < num[i+1] + num[i+2]:
        print(num[i] + num[i+1] + num[i+2])
        flag = 0
        break

if flag == 1:
    print(-1)
