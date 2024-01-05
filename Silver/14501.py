# n = int(input())
# timelist = []
# for i in range(n):
#     a,b = map(int, input().split())
#     timelist.append([a,b])
# # print(timelist)

# max_money = 0
# visit =[0]*n
# for i in range(n-1):
#     if visit[i] == 0:
#         start = i + 1
#         money = timelist[i][1]
#         time = timelist[i][0]
#         while True:
#             if start + time >= n:
#                 if start + time == n and  timelist[n-1][0] == 1:
#                     money += timelist[n-1][1]
#                 break
#             else:
#                 start += time
#                 money += timelist[start-1][1]
#                 a = timelist[start-1][0]
#     # print(money)
#     if money >= max_money:
#         max_money = money

# print(max_money)

    




n = int(input())
list1 = []
for _ in range(n):
    list1.append(list(map(int,input().split())))

dp = [0]*(n+1)

for i in range(n):
    for j in range(i + list1[i][0],n+1):
        if dp[j] < dp[i] + list1[i][1]:
            dp[j] = dp[i] + list1[i][1]
print(max(dp))