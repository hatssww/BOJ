import sys
input = sys.stdin.readline
mod = 1000000009
d = [0, 1, 2, 4] * (1000000 - 3)
t = int(input())
A = []
for _ in range(t):
    A.append(int(input()))
n = max(A)
for i in range(4, n+1):
    d[i] = (d[i-1] + d[i-2] + d[i-3]) % mod

for i in A:
    print(d[i] % mod)