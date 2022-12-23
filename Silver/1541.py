problem = list(input().split('-'))
for i in range(len(problem)):
    if '+' in problem[i]:
        num = 0
        s = list(problem[i].split('+'))
        for j in range(len(s)):
            num += int(s[j])
        problem[i] = num
answer = int(problem[0])
for i in range(1,len(problem)):
    answer -= int(problem[i])
print(answer)