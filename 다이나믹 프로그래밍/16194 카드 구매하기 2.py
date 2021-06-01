import sys

n = int(sys.stdin.readline())
p = [0] + list(map(int, sys.stdin.readline().split()))
d = [0] + [10000] * n
d[1] = p[1]

for i in range(2, n + 1):
    for j in range(1, i + 1):
        if d[i] > d[i - j] + p[j]:
            d[i] = d[i - j] + p[j]

print(d[n])