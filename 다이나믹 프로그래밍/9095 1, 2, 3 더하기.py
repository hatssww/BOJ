import sys

t = int(sys.stdin.readline())

N = [int(sys.stdin.readline()) for _ in range(t)]
m = max(N)

d = [0, 1, 2, 4] * (m - 3)

for n in N:
    for i in range(4, n + 1):
        d[i] = d[i - 1] + d[i - 2] + d[i - 3]
    print(d[n])