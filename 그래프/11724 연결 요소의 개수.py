import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
res = set()
for _ in range(m):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(V):
    visited = [False] * (n + 1)
    tmp = []
    queue = deque()
    queue.append(V)
    visited[V] = True
    while queue:
        V = queue.popleft()
        tmp.append(V)
        for i in graph[V]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    tmp.sort()
    res.add(tuple(tmp))

for i in range(1, n + 1):
    bfs(i)

print(len(res))