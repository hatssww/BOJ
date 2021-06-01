import sys

n = int(sys.stdin.readline())
a = [0] + list(map(int, sys.stdin.readline().split()))
d = [0] * (n + 1)
result = -1001
for i in range(1, n + 1):
    d[i] = max(d[i-1] + a[i], a[i])
    result = max(result, d[i])

print(result)