import sys

n = int(sys.stdin.readline())
postfix = sys.stdin.readline().rstrip()
stack = []
number = [int(sys.stdin.readline()) for i in range(n)]

for ch in postfix:
    if ch.isalpha():
        stack.append(number[ord(ch) - ord('A')])
    else:
        num2 = stack.pop()
        num1 = stack.pop()
        if ch == '+':
            stack.append(num1 + num2)
        elif ch == '-':
            stack.append(num1 - num2)
        elif ch == '*':
            stack.append(num1 * num2)
        elif ch == '/':
            stack.append(round(num1 / num2, 2))

print(f'{stack[0]:.2f}')