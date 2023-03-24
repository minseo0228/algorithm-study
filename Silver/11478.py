from itertools import combinations
string = input()
result = []
for i in range(len(string)):
    a = string[i]
    result.append(a)
    for j in range(i+1,len(string)):
        a += string[j]
        result.append(a)
result  = set(result)
print(len(result))