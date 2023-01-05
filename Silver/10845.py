from collections import deque
import sys
queue = deque()
N = int(sys.stdin.readline())
for i in range(N):
    inp = sys.stdin.readline().strip().split()
    if len(inp) == 1:
        if inp[0] == 'empty':
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif inp[0] == 'size':
            print(len(queue))
        elif inp[0] == 'front':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
        elif inp[0] == 'back':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[len(queue)-1])
        else:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue.popleft())
    else:
        a = inp[0] 
        b = int(inp[1])
        if a == 'push':
            queue.append(b)

