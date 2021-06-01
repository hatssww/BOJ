import sys


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


n = int(sys.stdin.readline())
f = str(factorial(n))
count = 0
for i in f[::-1]:
    if i == '0':
        count += 1
    else:
        break
print(count)