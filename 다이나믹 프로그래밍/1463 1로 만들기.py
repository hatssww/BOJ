import sys

x = int(sys.stdin.readline())

dp = [0] * (x + 1)

for n in range(2, x + 1):
    dp[n] = dp[n - 1] + 1

    if n % 2 == 0:
        dp[n] = min(dp[n//2] + 1, dp[n])
    if n % 3 == 0:
        dp[n] = min(dp[n//3] + 1, dp[n])

print(dp[x])