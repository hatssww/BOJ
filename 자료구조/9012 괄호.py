import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    stack =[]
    vps = input().rstrip()
    check = 0
    for i in vps:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0:
                stack.pop(-1)
            else:
                print("NO")
                check = 1
                break
    
    if len(stack) == 0 and check == 0:
        print("YES")
    elif len(stack) != 0 and check == 0:
        print("NO")