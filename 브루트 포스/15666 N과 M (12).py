# # DFS를 이용한 백트래킹
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# N = list(map(int, input().split()))
# N.sort()
# stack = []

# def dfs(depth, k, n, m):
#     if depth == m:
#         print(' '.join(map(str, stack)))
#         return
    
#     over = 0
#     for i in range(k, n):
#         if over != N[i]:
#             stack.append(N[i])
#             over = N[i]
#             dfs(depth + 1, i, n, m)
#             stack.pop()

# dfs(0, 0, n, m)


# 라이브러리를 이용한 풀이
from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
N = list(map(int, input().split()))
N.sort()
c = set(combinations_with_replacement(N, m))
c = list(c)
c.sort()

for i in c:
    print(' '.join(map(str, i)))