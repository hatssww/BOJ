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
#         stack.append(i)
#         dfs(i)
#         stack.pop()

# dfs(1)


# 라이브러리를 이용한 풀이
from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
c = combinations_with_replacement(range(1, n + 1), m)

for i in c:
    print(' '.join(map(str, i)))