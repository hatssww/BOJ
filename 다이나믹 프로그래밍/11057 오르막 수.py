import sys
input = sys.stdin.readline
n = int(input())
mod = 10007

d = [[0] * 10 for i in range(1001)]
for i in range(10):
    d[1][i] = 1

for i in range(2, 1001):
    for j in range(10):
        for k in range(j + 1):
            d[i][j] += d[i-1][k]

print(sum(d[n]) % mod)