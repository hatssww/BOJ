import sys

stick = sys.stdin.readline().rstrip()
stack = []
result = 0
for i in range(len(stick)):
    if stick[i] == "(":
        stack.append("(")
    elif stick[i] == ")":
        if stick[i-1] == "(":
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)