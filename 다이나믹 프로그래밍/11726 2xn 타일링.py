import sys

n = int(sys.stdin.readline())
d = [0, 1, 2] + [0] * (n - 2)
for i in range(3, n + 1):
    d[i] = d[i-1] + d[i-2]
print(d[n] % 10007)