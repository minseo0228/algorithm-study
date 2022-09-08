while True:
    a = input()
    if a == '0':
        break
    if a[::-1]==a:
        print("yes")
    else:
        print("no")