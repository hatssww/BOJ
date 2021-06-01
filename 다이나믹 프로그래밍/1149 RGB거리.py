import sys
input = sys.stdin.readline
n = int(input())
d = [[0] * 4 for i in range(n + 1)]

for i in range(1, n + 1):
    d[i] = [0] + list(map(int, input().split()))

for i in range(2, n + 1):
    d[i][1] = d[i][1] + min(d[i-1][2], d[i-1][3])
    d[i][2] = d[i][2] + min(d[i-1][1], d[i-1][3])
    d[i][3] = d[i][3] + min(d[i-1][1], d[i-1][2])

print(min(d[n][1:]))