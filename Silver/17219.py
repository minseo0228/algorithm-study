N,M = map(int,input().split())
password = {}
for i in range(N):
    list1 = input().split()
    name, passw = list1[0], list1[1]
    password[name] = passw
for i in range(M):
    find = input()
    print(password[find])