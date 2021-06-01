import sys

n = int(sys.stdin.readline())

d = [0, 1, 3] + [0] * (n - 2)

for i in range(3, n + 1):
    d[i] = d[i-2] * 2 + d[i - 1]

print(d[n] % 10007)