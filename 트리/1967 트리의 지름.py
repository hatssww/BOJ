import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

n = int(input())
node = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    parent, child, cost = map(int, input().split())
    node[parent].append([child, cost])
    node[child].append([parent, cost])

dp1 = [0] * (n + 1)

def dfs(dp, x):
    for i in node[x]:
        nx = i[0]
        if dp[nx] == 0:
            dp[nx] = dp[x] + i[1]
            dfs(dp, nx)

for i in range(1, n + 1):
    if len(node[i]) == 1:
        start_node = i
        break

if n == 1:
    print(0)
else:
    dfs(dp1, start_node)
    dp1[start_node] = 0
    dp2 = [0] * (n + 1)
    dfs(dp2, dp1.index(max(dp1)))
    dp2[dp1.index(max(dp1))] = 0
    print(max(dp2))