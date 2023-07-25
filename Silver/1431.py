n = int(input())
l = []
def countnum(x):
    count = 0
    x = str(x)
    for i in x:
        if '0'<=i<='9':
            count += int(i)
    return count

for i in range(n):
    l.append(input())
l.sort()
for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            if len(l[j]) > len(l[j + 1]):
                l[j], l[j + 1] = l[j + 1], l[j]
            if  len(l[j]) == len(l[j + 1]):
                if countnum(l[j]) > countnum(l[j+1]):
                    l[j], l[j + 1] = l[j + 1], l[j]

for i in l:
    print(i)