scoresum = 0
nsum = 0
for i in range(20):
    sub,num,score = input().split()
    nsum += float(num)
    if score == 'A+':
        scoresum += 4.5*float(num)
    elif score == 'A0':
        scoresum += 4*float(num)
    elif score == 'B+':
        scoresum += 3.5*float(num)
    elif score == 'B0':
        scoresum += 3*float(num)
    elif score == 'C+':
        scoresum += 2.5*float(num)
    elif score == 'C0':
        scoresum += 2*float(num)
    elif score == 'D+':
        scoresum += 1.5*float(num)
    elif score == 'D0':
        scoresum += float(num)
    elif score == 'P':
        nsum -= float(num)
grade = scoresum/nsum
print(grade)
