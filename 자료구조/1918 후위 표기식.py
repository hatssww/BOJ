import sys

postfix = sys.stdin.readline().rstrip()
result = ""
priority = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0
}
stack = []

for ch in '('+postfix+')':
    if ch.isalpha():
        result += ch
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        while True:
            x = stack.pop()
            if x == '(':
                break
            result += x
    else:
        while stack[-1] != '(' and priority[ch] <= priority[stack[-1]]:
            result += stack.pop()
        stack.append(ch)

print(result)