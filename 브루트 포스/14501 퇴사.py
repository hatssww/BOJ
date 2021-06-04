import sys
input = sys.stdin.readline

n = int(input())
table = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
dp = [0] * 16

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i-1])
    
    if i + table[i][0] - 1 <= n:
        dp[i + table[i][0] - 1] = max(dp[i + table[i][0] - 1], dp[i - 1] + table[i][1])

print(dp[n])