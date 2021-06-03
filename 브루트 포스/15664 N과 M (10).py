# # DFS를 이용한 백트래킹
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# N = list(map(int, input().split()))
# N.sort()
# visited = [False] * n
# stack = []

# def dfs(depth, k, n, m):
#     if depth == m:
#         print(' '.join(map(str, stack)))
#         return
    
#     over = 0
#     for i in range(k, n):
#         if not visited[i] and over != N[i]:
#             visited[i] = True
#             stack.append(N[i])
#             over = N[i]
#             dfs(depth + 1, i + 1, n, m)
#             visited[i] = False
#             stack.pop()

# dfs(0, 0, n, m)


# 라이브러리를 이용한 풀이
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
N = list(map(int, input().split()))
N.sort()
c = set(combinations(N, m))
c = list(c)
c.sort()

for i in c:
    print(' '.join(map(str, i)))