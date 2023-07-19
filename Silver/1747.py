n = int(input())
def is_prime(x):
    for i in range(2,x):
        if x % i == 0:
            return(-1)
    return(0)

result = 0
for i in range(n,1004000):
    if i == 1:
        continue
    if is_prime(i)==0 and str(i) == str(i)[::-1]:
        result = i
        break
print(result)

# if n == 1:
#     print(2)
# else:
#     for i in range(n,1004000):
#         if prime(i)==0:
#             check = 0
#             num = str(i)
#             for j in range(len(num)//2):
#                 if num[j] != num[len(num)-1]:
#                     check = 1
#             if check == 0:
#                 print(i)
#                 break