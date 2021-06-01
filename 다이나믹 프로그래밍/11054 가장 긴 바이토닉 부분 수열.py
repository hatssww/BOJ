import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
B = A.copy()
B.reverse()

dp = [1] * n
dm = [1] * n

for i in range(n):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[j] + 1, dp[i])
        if B[j] < B[i]:
            dm[i] = max(dm[j] + 1, dm[i])

dm.reverse()
result = []
for i in range(n):
    result.append(dp[i] + dm[i])

print(max(result) - 1)