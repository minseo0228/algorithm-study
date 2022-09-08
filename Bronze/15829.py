l = int(input())
a = input()
sum = 0
for i in range(l):
    sum += (ord(a[i])-96)*31**i
print(sum%1234567891)