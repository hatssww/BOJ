# # DFS를 이용한 백트래킹
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# N = list(map(int, input().split()))
# N.sort()
# stack = []

# def dfs(k):
#     if len(stack) == m:
#         print(' '.join(map(str, stack)))
#         return

#     for i in range(k, n):
#         stack.append(N[i])
#         dfs(i)
#         stack.pop()

# dfs(0)


# 라이브러리를 이용한 풀이
from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
N = list(map(int, input().split()))
N.sort()
c = combinations_with_replacement(N, m)

for i in c:
    print(' '.join(map(str, i)))