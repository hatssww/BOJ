n = int(input())

no_message = False
count = 0
result = []
stack = []

for x in range(n):
    x = int(input())
    while count < x:
        count += 1
        stack.append(count)
        result.append("+")
    
    if stack[-1] == x:
        stack.pop()
        result.append("-")
    else:
        no_message = True
        break

if no_message:
    print("NO")
else:
    print('\n'.join(result))