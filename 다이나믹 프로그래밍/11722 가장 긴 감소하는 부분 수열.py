import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
d = [1] * (n + 1)
for i in range(n):
    for j in range(i):
        if A[j] > A[i]:
            d[i] = max(d[j] + 1, d[i])

print(max(d))