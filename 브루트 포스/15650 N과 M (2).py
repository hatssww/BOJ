# # DFS를 이용한 백트래킹
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# stack = []

# def dfs(k):
#     if len(stack) == m:
#         print(' '.join(map(str, stack)))
#         return
#     for i in range(k, n + 1):
#         if i in stack:
#             continue
#         stack.append(i)
#         dfs(i + 1)
#         stack.pop()

# dfs(1)


# 라이브러리 이용
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
c = combinations(range(1, n + 1), m)

for i in c:
    print(' '.join(map(str, i)))