# 런타임 에러 (RecursionError) 발생하지만 제한 풀어주면 채점되어 정답 처리됨.
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

n = int(input())
node = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
for _ in range(n - 1):
    x, y = map(int, input().strip().split())
    node[x].append(y)
    node[y].append(x)

def find_parent(idx):
    if not node[idx]:
        return
    for i in node[idx]:
        if not parent[i]:
            parent[i] = idx
            find_parent(i)


for i in range(1, n + 1):
    if node[i]:
        find_parent(i)

for i in range(2, n + 1):
    print(parent[i])