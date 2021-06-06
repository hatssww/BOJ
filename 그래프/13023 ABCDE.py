# # 정답은 나오지만 런타임 에러 (RecursionError) 발생
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# dp = [[0] * n for _ in range(n)]

# for i in range(m):
#     x, y = map(int, input().split())
#     dp[x][y], dp[y][x] = 1, 1

# tmp = [x]
# ans = [i for i in range(n)]
# is_true = False
# def solve(s):
#     global tmp, ans, is_true
#     if len(tmp) == n + 1:
#         res = tmp[1:]
#         res.sort()
#         if res == ans:
#             is_true = True
#         return
#     for j in range(n):
#         if dp[s][j] == 1:
#             tmp.append(j)
#             solve(j)
#             tmp.pop()
# solve(x)
# if is_true:
#     print(1)
# else:
#     print(0)


# 인접 리스트 방식 이용
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    x, y = map(int, input().rstrip().split())
    arr[x].append(y)
    arr[y].append(x)


def dfs(depth, idx):
    if depth == 4:
        print(1)
        exit()
    for i in arr[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i)
            visited[i] = False


for i in range(n):
    visited[i] = True
    dfs(0, i)
    visited[i] = False

print(0)