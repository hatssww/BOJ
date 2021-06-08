import sys
input = sys.stdin.readline

v = int(input())
node = [[] for _ in range(v + 1)]
for _ in range(v):
    tmp = list(map(int, input().split()))
    i = 1
    while tmp[i] != -1:
        node[tmp[0]].append([tmp[i], tmp[i + 1]])
        i += 2

dp1 = [0] * (v + 1)

def dfs(dp, x):
    for i in node[x]:
        nx = i[0]
        if dp[nx] == 0:
            dp[nx] = dp[x] + i[1]
            dfs(dp, nx)


dfs(dp1, 1)
dp1[1] = 0
dp2 = [0] * (v + 1)
dfs(dp2, dp1.index(max(dp1)))
dp2[dp1.index(max(dp1))] = 0
print(max(dp2))