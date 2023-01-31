a,b = input().split()
if len(a) != len(b):
    print(0)
else:
    c = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            if a[i] == '8':
                c += 1
        else:
            break
    print(c)

   