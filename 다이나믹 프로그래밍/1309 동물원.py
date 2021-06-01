import sys
input = sys.stdin.readline
n = int(input())

mod = 9901
d = [[0] * 3 for i in range(100001)]

for i in range(3):
    d[1][i] = 1

for i in range(2, 100001):
    d[i][0] = (d[i-1][0] + d[i-1][1] + d[i-1][2]) % mod
    d[i][1] = (d[i-1][0] + d[i-1][2]) % mod
    d[i][2] = (d[i-1][0] + d[i-1][1]) % mod

print(sum(d[n]) % mod)