import sys

n = int(sys.stdin.readline())
A = [0] + list(map(int, sys.stdin.readline().split()))

d = [1] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i):
        if A[i] > A[j]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))