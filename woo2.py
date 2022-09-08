# list2 = []
# list1 = []
# final = 0
# def finalscore():
#     final = b*0.1 +c*0.2 + d*0.3 +e*0.4
#     return final
# def grade(num):
#     print("+++++++++++num")
#     print(num)
#     d = sorted(data.items(), key = lambda x :x[1], reverse = True)
#     print(d)
#     for i in range(len(d)):
#         print("#######")
#         print(i)
#         if i < num*0.2:
#             print(d[i][0],"A")
#         elif i< (num*0.5) and i> (num*0.2):
#             print(d[i][0],"B")
#         elif i< (num*0.8) and i> (num*0.5):
#             print(d[i][0],"C")
#         elif i< (num*0.9) and i >(num*0.8):
#              print(d[i][0],"D")
#         else:
#              print(d[i][0],"F")
# data = {}
# num = int(input())
# for i in range(num):
#     a,b,c,d,e = map(int,(input().split()))
#     list1 = [a,b,c,d,e]
#     final1 = finalscore()
#     final1 = int(final1)
#     list1.append(final1)
#     list2.append(list1)
#     data[list1[0]] = final1
# key = input()
# if key == 'num':
#     d = sorted(data.items())
#     for i in range(len(d)):
#         print(d[i][0])
# elif key == 'grade':
#     grade(num)

list2 = []
list1 = []
final = 0
def finalscore():
    final = b*0.1 +c*0.2 + d*0.3 +e*0.4
    return final
def grade():
    d = sorted(data.items(), key = lambda x :x[1], reverse = True)
    for i in range(len(d)):
        if i < (num*0.2):
            print(d[i][0],"A")
        elif i< (num*0.5) and i> (num*0.2):
            print(d[i][0],"B")
            d[i].append("B")
        elif i< (num*0.8) and i> (num*0.5):
            print(d[i][0],"C")
        elif i< (num*0.9) and i >(num*0.8):
             print(d[i][0],"D")
        else:
             print(d[i][0],"F")
    d = sorted(key = lambda x:x[1])
    print(d)
data = {}
num = int(input())
for i in range(num):
    a,b,c,d,e = map(int,(input().split()))
    list1 = [a,b,c,d,e]
    final1 = finalscore()
    final1 = int(final1)
    list1.append(final1)
    list2.append(list1)
    data[list1[0]] = final1
key = input()
if key == 'num':
    d = sorted(data.items())
    for i in range(len(d)):
        print(d[i][0])
elif key == 'grade':
    grade()
