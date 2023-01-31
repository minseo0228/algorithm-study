a,b = input().split()
# def search(x):
#     count = 0
#     for i in x:
#         if i == '8':
#             count += 1
#     return count
# num = 9999
if len(a) != len(b):
    print(0)
else:
    c = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            if a[i] == '8':
                c += 1
    if a[0] != b[0]:
        c -= 1
    print(c)

# if len(a) <= 1:
#     print(0)
# elif len(a) != len(b):
#     for i in range(int(a),int(b)+1):
#         num = min(search(str(i)),num)
#     print(num)
# else:
#     c = 0
#     for i in range(len(a)):
#         if a[i] == b[i] and a[i] == '8':
#             c += 1
#         elif a[i] == b[i]:
#             continue
#         else:
#             for j in range():
#                 num = min(search(str(j)),num)
#     print(c+num)
     
   