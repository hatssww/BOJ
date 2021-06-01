import sys
mod = 1000000000
max = 200
n, k = map(int, sys.stdin.readline().split())

d = [[0] * (max + 1) for i in range(max + 1)]

for i in range(max + 1):
    d[1][i] = 1
    d[2][i] = i + 1

for i in range(2, max + 1):
    d[i][1] = i
    for j in range(2, max + 1):
        d[i][j] = d[i-1][j] + d[i][j-1] % mod

print(d[k][n] % mod)