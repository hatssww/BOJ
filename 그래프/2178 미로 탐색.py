import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = [[x, y]]
    visited[x][y] = 1
    while queue:
        x, y = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n - 1 and 0 <= ny <=  m - 1:
                if visited[nx][ny] == False and M[nx][ny] != '0':
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])


n, m = map(int, input().split())

M = [input().rstrip() for _ in range(n)]
visited = [[False] * m for _ in range(n)]

bfs(0, 0)
print(visited[n-1][m-1])