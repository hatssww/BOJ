# # DFS를 이용한 백트래킹
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# stack = []

# def dfs():
#     if len(stack) == m:
#         print(' '.join(map(str, stack)))
#         return
#     for i in range(1, n + 1):
#         if i in stack:
#             continue
#         stack.append(i)
#         dfs()
#         stack.pop()

# dfs()


# 라이브러리 이용
from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = permutations(range(1, n + 1), m)

for i in p:
    print(' '.join(map(str, i)))