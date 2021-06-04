import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
S = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

combs = list(combinations(range(n), n//2))

for i in range(n):
    for j in range(n):
        if not dp[i][j] or not dp[j][i]:
            dp[i][j], dp[j][i] = S[i][j] + S[j][i], S[i][j] + S[j][i]


def sum(c):
    sum = 0
    for i in range(len(c)):
        for j in range(i + 1, len(c)):
            sum += dp[c[i]][c[j]]
    return sum

total = [i for i in range(n)]
result = sys.maxsize
for c in combs:
    others = set(total) - set(list(c))
    o = list(others)
    result = min(result, abs(sum(c) - sum(o)))

print(result)