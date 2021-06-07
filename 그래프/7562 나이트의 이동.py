from collections import deque
import sys
input = sys.stdin.readline

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]


def bfs(a, b):
    chess[a][b] = 1
    queue.append([a, b])
    while queue:
        x, y = queue.popleft()
        if x == goal_x and y == goal_y:
            return chess[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= L - 1 and 0 <= ny <= L - 1:
                if chess[nx][ny] == 0:
                    chess[nx][ny] = chess[x][y] + 1
                    queue.append([nx, ny])

t = int(input())
for _ in range(t):
    L = int(input())
    chess = [[0] * L for _ in range(L)]
    a, b = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    queue = deque()

    print(bfs(a, b))