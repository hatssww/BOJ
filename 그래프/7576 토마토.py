from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n - 1 and 0 <= ny <= m - 1:
                if box[nx][ny] == 0:
                    box[nx][ny] = box[x][y] + 1
                    queue.append([nx, ny])

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])

bfs()

is_true = False
result = -2

for i in box:
    for j in i:
        if j == 0:
            is_true = True
        result = max(result, j)

if is_true:
    print(-1)
elif result == -1:  # 안익은게 하나라도 있으면 0이 존재해서 -1이 출력되고, 1이 최댓값인 경우도 결과에서 -1을 하므로 0이 출력됨. -1만 있는 경우에 -2가 출력되지 않게 하기 위해 정해놓은 조건문임.
    print(0)
else:
    print(result - 1)