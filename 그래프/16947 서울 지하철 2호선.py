import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for i in range(n + 1)]
visited = [0] * (n + 1)
dist = [0] * (n + 1)

for i in range(n):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v, cnt):
    if visited[v]:
        if cnt - dist[v] >= 3:
            return v
        else:
            return -1
    visited[v] = 1
    dist[v] = cnt
    for i in graph[v]:
        cycle_start = dfs(i, cnt + 1)
        if cycle_start != -1:
            visited[v] = 2
            if v == cycle_start:
                return -1
            else:
                return cycle_start
    return -1


dfs(1, 0)

queue = deque()
for i in range(1, n + 1):
    if visited[i] == 2:
        queue.append(i)
        dist[i] = 0
    else:
        dist[i] = -1

while queue:
    x = queue.popleft()
    for y in graph[x]:
        if dist[y] == -1:
            queue.append(y)
            dist[y] = dist[x] + 1

print(" ".join(map(str, dist[1:])))