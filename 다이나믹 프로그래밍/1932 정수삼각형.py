import sys
input = sys.stdin.readline
n = int(input())
A = [[0] + list(map(int, input().split())) for _ in range(n)]
d = [[0] + [0] * i + [0] for i in range(n + 1)]

d[1][1] = A[0][1]

for i in range(2, n + 1):
    for j in range(1, i + 1):
        d[i][j] = max(A[i-1][j] + d[i-1][j-1], A[i-1][j] + d[i-1][j])

print(max(d[n]))