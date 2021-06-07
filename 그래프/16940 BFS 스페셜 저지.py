# 일반적인 BFS
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

ans = list(map(int, input().split()))
visited = [False] * (n + 1)

def bfs(start):
    if start != 1:
        return 0
    queue = deque([start])
    visited[start] = True
    idx = 1
    while queue:
        v = queue.popleft()
        if not graph[v]:
            continue
        next = []
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                next.append(i)
        for j in range(idx, idx + len(next)):
            if ans[j] in next:
                queue.append(ans[j])
            else:
                return 0
        idx += len(next)
    
    return 1


print(bfs(ans[0]))


# 집합을 이용한 풀이
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    graph = [set() for _ in range(n + 1)]
    graph[0].add(1)
    for _ in range(n - 1):
        x, y = map(int, input().split())
        graph[x].add(y)
        graph[y].add(x)
    print(graph)
    queue = [0]
    idx = 0
    ans = list(map(int, input().split()))
    for i in ans:
        while i not in graph[queue[idx]]:  # i가 해당 그래프 연결리스트에 들어있으면 queue에 정답으로 추가, 없으면 idx 증가, idx 만큼 수행했는데도 답이 아니면 queue의 인덱스를 벗어나는 것이므로 오답 처리
            idx += 1
            if idx == len(queue):
                return 0
        queue.append(i)
        print(queue, idx)

    return 1


print(solve())