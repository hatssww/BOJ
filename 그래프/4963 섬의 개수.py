# # DFS를 이용한 풀이(런타임 에러 (RecursionError))
# import sys
# input = sys.stdin.readline

# dx = [-1, 1, 0, 0, -1, -1, 1, 1]
# dy = [0, 0, -1, 1, -1, 1, -1, 1]

# def dfs(M, visited, x, y):
#     visited[x][y] = True
#     for i in range(8):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx <= h - 1 and 0 <= ny <=  w - 1:
#             if not visited[nx][ny] and M[nx][ny] != 0:
#                 dfs(M, visited, nx, ny)
#     return True

# while True:
#     w, h = map(int, input().split())
#     if w == 0 and h == 0:
#         break
    
#     M = [list(map(int, input().split())) for _ in range(h)]
#     visited = [[False] * w for _ in range(h)]
#     cnt = 0

#     for i in range(h):
#         for j in range(w):
#             if M[i][j] == 0:
#                 continue
#             if not visited[i][j]:
#                 if dfs(M, visited, i, j):
#                     cnt += 1

#     print(cnt)


# BFS를 이용한 풀이
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(M, visited, x, y):
    queue = [[x, y]]
    visited[x][y] = True
    while queue:
        x, y = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= h - 1 and 0 <= ny <=  w - 1:
                if not visited[nx][ny] and M[nx][ny] != 0:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    M = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if M[i][j] == 0:
                continue
            if not visited[i][j]:
                bfs(M, visited, i, j)
                cnt += 1

    print(cnt)