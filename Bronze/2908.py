a,b =input().split()
a = list(a)
b = list(b)
for i in range (3):
    a[i] = int(a[i])
for i in range (3):
    b[i] = int(b[i])
a1 = a[2]*100 +a[1]*10+a[0]
b1 = b[2]*100+b[1]*10+b[0]
if(a1>b1):
    print(a1)
else:
    print(b1)
