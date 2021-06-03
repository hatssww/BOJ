# # DFS를 이용한 백트래킹
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# N = list(map(int, input().split()))
# N.sort()
# stack = []

# def dfs():
#     if len(stack) == m:
#         print(' '.join(map(str, stack)))
#         return

#     for i in range(n):
#         if N[i] in stack:
#             continue
#         stack.append(N[i])
#         dfs()
#         stack.pop()

# dfs()


# 라이브러리를 이용한 풀이
from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
N = list(map(int, input().split()))
N.sort()
p = permutations(N, m)

for i in p:
    print(' '.join(map(str, i)))