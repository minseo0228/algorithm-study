first = input()
second = input()
# 글자가 같은 경우 -> 글자를 추가하기 전 값 + 1
# 글자가 다른 경우 -> 가장 큰 값으로 dp값 바꾸기
dp = [0]*(len(first)+len(second))

for i in range(len(first)):
    count = 0
    for j in range(len(second)):
        if count < dp[j]:
            count = dp[j]
        elif first[i] == second[j]:
            dp[j] = count +1

print(max(dp))
                


# def search(a):
#     count = 0
#     queue = deque()
#     queue.append(a,0)
#     while queue:
#         x, index = queue.popleft()
#         for i in range(index,len(second)):
#             if second[i] == x:
#                 count += 1
#                 queue.append()
        

# result = []
# for i in first:
#     result.append(search(i))
# print(max(result))
