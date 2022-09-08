# num = int(input())
# count = 0
# n = 0
# for i in range(pow(10,num)):
#     i = str(i)
#     for j in range(len(i)-1):
#         if int(i[j]) <= int(i[j+1]):
#             n +=1
#         else:
#             break
#         if n == len(i)-1:
#             count += 1
#     n = 0
# print(count+10)

n = int(input())
dp=[1]*(10)
for i in range(n-1):
    for j in range(1,10):
        dp[j]+=dp[j-1]
        print(dp[j])
print(sum(dp)%10007)
