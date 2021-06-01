import sys

n = int(sys.stdin.readline())

d = [1] * (n + 1)
A = [0] + list(map(int, sys.stdin.readline().split()))
for i in range(1, n + 1):
    for j in range(1, i):
        if A[i] > A[j]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))

order = max(d)
result = []
for i in range(n, -1, -1):
    if d[i] == order:
        result.append(A[i])
        order -= 1
result.reverse()
for i in result:
    print(i, end=" ")