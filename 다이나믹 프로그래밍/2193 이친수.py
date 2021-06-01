import sys

d = [[0, 0] for i in range(91)]
d[1][1] = 1
d[2][0] = 1

n = int(sys.stdin.readline())
for i in range(3, n + 1):
    for j in range(2):
        d[i][j] = d[i - 1][j] + d[i - 2][j]

print(sum(d[n]))