from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
maze = [[] * m for _ in range(n)]
s = [input().rstrip() for _ in range(n)]
for i in range(n):
    for j in range(m):
        maze[i].append(int(s[i][j]))

visited = [[False] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    visited[0][0] = True
    q = deque([[0, 0]])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dp[nx][ny] = dp[x][y]
                    q.appendleft([nx, ny])
                if maze[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dp[nx][ny] = dp[x][y] + 1
                    q.append([nx, ny])

bfs()
print(dp[n-1][m-1])