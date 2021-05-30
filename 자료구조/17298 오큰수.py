import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
stack = [0]
result = [-1] * n

i = 1
while stack and i < n:
    while stack and A[stack[-1]] < A[i]:
        result[stack[-1]] = A[i]
        stack.pop()
    stack.append(i)
    i += 1

for i in range(n):
    print(result[i], end=" ")