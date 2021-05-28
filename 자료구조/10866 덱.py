import sys
from collections import deque

n = int(sys.stdin.readline())

d = deque()
for _ in range(n):
    com = list(map(str, sys.stdin.readline().split()))
    
    if com[0] == "push_front":
        d.appendleft(int(com[1]))
    elif com[0] == "push_back":
        d.append(int(com[1]))
    elif com[0] == "pop_front":
        if not d:
            print(-1)
        else:
            print(d.popleft())
    elif com[0] == "pop_back":
        if not d:
            print(-1)
        else:
            print(d.pop())
    elif com[0] == "size":
        print(len(d))
    elif com[0] == "empty":
        if not d:
            print(1)
        else:
            print(0)
    elif com[0] == "front":
        if not d:
            print(-1)
        else:
            print(d[0])
    elif com[0] == "back":
        if not d:
            print(-1)
        else:
            print(d[-1])