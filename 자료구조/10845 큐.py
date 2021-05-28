from collections import deque
import sys

n = int(sys.stdin.readline().strip())
queue = deque()

for _ in range(n):
    com = list(map(str, sys.stdin.readline().split()))
    
    if com[0] == 'push':
        queue.append(int(com[1]))
    elif com[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif com[0] == 'size':
        print(len(queue))
    elif com[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif com[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])