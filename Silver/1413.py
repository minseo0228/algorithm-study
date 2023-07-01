N = int(input())
serial = []
for i in range(N):
    serial.append(input())
serial.sort(key = len)