a = int(input())
sum = 0
list1 = []
for i in range(a):
    num = int(input())
    list1.append(num)
list1.sort(reverse=True)
for i in range(a):
    if i % 3 == 1 or i %3 == 0:
        sum = sum + list1[i]
print(sum)