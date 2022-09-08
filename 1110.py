# num = input()
# t = 0
# newnum = 0
# for i in range (100):
#     if num == newnum :
#         print(t)
#         exit()
#     else:
#          num = str(num)
#          new = int(num[0]) + int(num[1])
#          print(new)
#          print(type(new))
#          newnum = str(newnum)
#          newnum = num[1] + str(new)
#          new = newnum
#          t = t+1
#          newnum = int(newnum)
#          num = int(num)
# # num = int(input())
# # newnum = ''
# # t = 0
# # while num != newnum:
# #     num = str(num)
# #     new = int(num[0]) + int(num[1])
# #     new = str(new)
# #     newnum = num[1] + new[0]
# #     newnum = int(newnum)
# #     print(newnum)
# #     t =t+1
# # print(t)
# new = 0
# t = 0
# num = int(input())
# for i in range (100):
#     a = int(num/10)
#     b = int(num%10)
#     c = int((a+b)%10)
#     new = int(b*10 + c)
#     t = t+1
#     num = new
#     if (num == new):
#         break
# print(t)
# t = 0
# num = int(input())
# new = num

while True:
    a = new//10
    b = new%10
    c = (a+b)%10
    new = b*10 + c
    t+=1
    if (num == new):
        break
print(t)

num = int(input())
t = 0
new = num
for i in range(1000):
    a = new//10
    b = new%10
    c = (a+b)%10
    new = b*10 + c
    t = t+1
    if (num == new):
        break
print(t)