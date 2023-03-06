M,N = map(int,input().split())
prime = [0]*(N+1)
prime[0] = 1
prime[1] = 1
for i in range(2,N+1):
    for j in range(2,N+1):
        if i*j > N:
            break
        prime[i*j] = 1

for i in range(M,N+1):
    if prime[i] == 0:
        print(i)
