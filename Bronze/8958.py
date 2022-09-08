T = int(input())
point = 0
final = 0
for i in range(T):
    list1 = list(input())
    for j in range(len(list1)):
        if list1[j] == 'O':
            point = point +1
            final = final + point
        else:
            point = 0
    print(final)
    point = 0
    final = 0