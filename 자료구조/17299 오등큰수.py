import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
F = dict()
result = [-1] * n
stack = [0]

for i in A:
    try:
        F[i] += 1
    except:
        F[i] = 1

i = 1
while stack and i < n:
    while stack and F[A[stack[-1]]] < F[A[i]]:
        result[stack[-1]] = A[i]
        stack.pop()
    stack.append(i)
    i += 1

for i in range(n):
    print(result[i], end=" ")