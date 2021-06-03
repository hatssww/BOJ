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
#         stack.append(i)
#         dfs()
#         stack.pop()

# dfs()


# 라이브러리를 이용한 풀이
from itertools import product
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = product(range(1, n + 1), repeat=2)

for i in p:
    print(' '.join(map(str, i)))