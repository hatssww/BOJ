import sys
from collections import deque
input = sys.stdin.readline

k = int(input())

def bfs(start):
    visited[start] = 1
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = -visited[v]
                queue.append(i)
            else:
                if visited[i] == visited[v]:
                    return False
    return True


for i in range(k):
    v, e = map(int, input().split())
    is_true = True
    graph = [[] for i in range(v + 1)]
    visited = [0] * (v + 1)

    for j in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    for k in range(1, v + 1):
        if visited[k] == 0:
            if not bfs(k):
                is_true = False
                break
    print("YES" if is_true else "NO")