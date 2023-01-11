N,K = map(int,input().split())
valueList = []
for i in range(N):
    valueList.append(list(map(int,input().split())))
result = [ [0]*(K+1) for _ in range(N+1)]
for i in range(1,N+1): #-해줘야해서 +1씩 해줘야함
    for j in range(1,K+1): #1부터k무게까지 표를 만들었으니 반복
        w = valueList[i-1][0]
        v = valueList[i-1][1]
        if j < w:
            result[i][j] = result[i-1][j]
        else:
            result[i][j] = max(result[i-1][j-w]+v,result[i-1][j])
print(result[N][K])
        
