import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

ans = list(map(int, input().split()))
d = {}
for i in range(len(ans)):  # 제시되는 정답 순서대로 딕셔너리 만들어서 그래프 탐색 순서 조정
    d[ans[i]] = i
for j in graph:
    j.sort(key=lambda x: d[x])

visited = [False] * (n + 1)
stack = []


def dfs(v):
    visited[v] = True
    stack.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
        

dfs(1)
print(1 if stack == ans else 0)