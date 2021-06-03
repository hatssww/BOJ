# # DFS를 이용한 백트래킹
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# N = list(map(int, input().split()))
# N.sort()
# stack = []

# def dfs(depth, n, m):
#     if depth == m:
#         print(' '.join(map(str, stack)))
#         return
    
#     over = 0
#     for i in range(n):
#         if over != N[i]:
#             stack.append(N[i])
#             over = N[i]
#             dfs(depth + 1, n, m)
#             stack.pop()

# dfs(0, n, m)


# 라이브러리를 이용한 풀이
from itertools import product
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
N = list(map(int, input().split()))
N.sort()
p = set(product(N, repeat=m))
p = list(p)
p.sort()

for i in p:
    print(' '.join(map(str, i)))