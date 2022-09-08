N = int(input())
i = 666
count = 0
while True:
    i = str(i)
    if '666' in str(i):
        count += 1
    if count == N:
        print(i)
        break
    i = int(i)
    i += 1