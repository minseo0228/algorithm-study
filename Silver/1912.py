num = int(input())
num_list = list(map(int, input().split()))
for i in range(1,num):
    num_list[i] = max(num_list[i],num_list[i-1]+num_list[i])
print(max(num_list))