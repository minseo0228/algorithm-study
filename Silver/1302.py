n = int(input())
dic = {}
for i in range(n):
    x = input()
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1
a = max(dic)
b = dic[a]

result = [] 
for i in dic:
    if dic[i] == b:
        result.append(i)
result.sort()
print(result[0])