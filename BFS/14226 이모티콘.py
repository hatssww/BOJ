# # 답은 맞는거 같은데 채점은 틀렸습니다 뜸
# from collections import deque
# import sys
# input = sys.stdin.readline

# s = int(input())
# dp = [0] * 2001
# q = deque()

# def bfs():
#     q.append(1)
#     clip = 0
#     while q:
#         x = q.popleft()
#         if x == s:
#             print(dp[x])
#             return x
#         for nx in (x - 1, x + clip, x * 2):
#             if 2 <= nx < 1001 and not dp[nx]:
#                 if nx == x * 2:
#                     clip = x
#                     dp[nx] = dp[x] + 2
#                 else:
#                     dp[nx] = dp[x] + 1
#                 q.append(nx)
#                 # print(x, nx, dp[nx])


# bfs()


from collections import deque
import sys
input = sys.stdin.readline

s = int(input())
check = [[-1] * (s + 1) for _ in range(s + 1)]

def bfs():
    q = deque()
    q.append([1, 0])
    check[1][0] = 0
    while q:
        x, y = q.popleft()
        if check[x][x] == -1:  # 클립보드에 복사하는 연산
            check[x][x] = check[x][y] + 1
            q.append([x, x])
        if x + y <= s and check[x + y][y] == -1:  # 붙여넣기 연산
            check[x + y][y] = check[x][y] + 1
            q.append([x + y, y])
        if x - 1 >= 0 and check[x - 1][y] == -1:  # 화면에서 -1 연산
            check[x - 1][y] = check[x][y] + 1
            q.append([x - 1, y])

bfs()

res = check[s][1]
for i in range(1, s):
    if check[s][i] != -1:
        res = min(check[s][i], res)

print(res)