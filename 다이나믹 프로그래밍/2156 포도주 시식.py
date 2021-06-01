import sys
input = sys.stdin.readline
n = int(input())
A = [0]
for _ in range(n):
    A.append(int(input()))

d = [0] * (n + 1)
d[1] = A[1]
if n > 1:
    d[2] = A[1] + A[2]
print(d)
for i in range(3, n + 1):
    case1 = A[i] + d[i-2]
    case2 = A[i] + A[i-1] + d[i-3]
    case3 = d[i-1]
    d[i] = max(case1, case2, case3)

print(d[n])