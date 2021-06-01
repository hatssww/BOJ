import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
d = [[0, 0] for i in range(n)]

d[0] = [A[0], -999999999]

for i in range(1, n):
    d[i][0] = max(A[i], d[i-1][0] + A[i])
    d[i][1] = max(d[i-1][0], d[i-1][1] + A[i])

result = -999999999
for i in range(n):
    result = max(result, max(d[i]))

print(result)