list2 = []
list1 = []
final = 0
def finalscore():
    final = b*0.1 +c*0.2 + d*0.3 +e*0.4
    return final
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
a = int(input())
print(data[a])

