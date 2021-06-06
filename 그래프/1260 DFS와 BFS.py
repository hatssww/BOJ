import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited_d = [False] * (n + 1)
visited_b = [False] * (n + 1)
queue = deque()

for _ in range(m):
    x, y = map(int, input().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

def dfs(idx):
    visited_d[idx] = True
    print(idx, end=" ")
    for i in graph[idx]:
        if not visited_d[i]:
            dfs(i)

def bfs(idx):
    queue.append(idx)
    visited_b[idx] = True
    while queue:
        idx = queue.popleft()        
        print(idx, end=" ")
        for i in graph[idx]:
            if not visited_b[i]:
                queue.append(i)
                visited_b[i] = True

dfs(v)
print()
bfs(v)