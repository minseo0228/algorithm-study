T = int(input())
def sum(x):
    if x == 1:
        return(1)
    if x == 2:
        return(2)
    if x == 3:
        return(4)
    total = sum(x-3) + sum(x-2) + sum(x-1)
    return(total)
for i in range(T):
    num = int(input())
    print(sum(num))