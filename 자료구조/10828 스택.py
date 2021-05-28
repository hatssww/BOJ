import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    X = list(map(str, sys.stdin.readline().split()))
    if X[0] == "push":
        x = int(X[1])
        stack.append(x)
    elif X[0] == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif X[0] == "size":
        print(len(stack))
    elif X[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif X[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])