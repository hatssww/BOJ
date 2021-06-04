# DFS를 이용한 백트래킹
import sys
input = sys.stdin.readline

n = int(input())
N = list(map(int, input().split()))
stack = []
visited = [False] * n
result = set()

def dfs(depth):
    if depth == n:
        result.add(tuple(stack))
        return
    over = 0
    for i in range(n):
        if not visited[i] and over != N[i]:
            visited[i] = True
            over = N[i]
            stack.append(N[i])
            dfs(depth + 1)
            visited[i] = False
            stack.pop()

dfs(0)

result = list(result)
max_dis = 0
for i in result:
    sum = 0
    for j in range(n - 1):
        sum += abs(i[j] - i[j + 1])
    max_dis = max(max_dis, sum)

print(max_dis)


# 라이브러리를 이용한 풀이
from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
N = list(map(int, input().split()))
p = permutations(N)

max_dis = 0
for i in p:
    print(i)
    sum = 0
    for j in range(n - 1):
        sum += abs(i[j] - i[j + 1])
    max_dis = max(max_dis, sum)

print(max_dis)