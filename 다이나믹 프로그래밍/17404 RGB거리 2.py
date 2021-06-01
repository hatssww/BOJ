import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
cost = [[0, 0, 0]]
for _ in range(n):
    c = list(map(int, input().split()))
    cost.append(c)

d = [[0, 0, 0] for _ in range(n + 1)]

result = INF
for first in range(3):
    for i in range(3):
        if first == i:
            d[1][i] = cost[1][i]
        else:
            d[1][i] = INF

    for i in range(2, n + 1):
        d[i][0] = cost[i][0] + min(d[i-1][1], d[i-1][2])
        d[i][1] = cost[i][1] + min(d[i-1][0], d[i-1][2])
        d[i][2] = cost[i][2] + min(d[i-1][0], d[i-1][1])

    for i in range(3):
        if i == first:
            continue
        result = min(result, d[n][i])

print(result)