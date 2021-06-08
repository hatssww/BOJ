from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
cnt = 1

def find_island(a, b, cnt):
    q = deque([[a, b]])
    visited[a][b] = cnt
    while q:
        x, y =  q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = cnt
                    q.append([nx, ny])

def bfs(num):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1 and visited[nx][ny] != num:
                    return check[x][y] - 1
                if arr[nx][ny] == 0 and check[nx][ny] == 0:
                    check[nx][ny] = check[x][y] + 1
                    queue.append([nx, ny])


for i in range(n):  # 같은 섬끼리 표시하기
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == 0:
            find_island(i, j, cnt)
            cnt += 1

ans = sys.maxsize
for c in range(1, cnt):  # 섬 크기를 넓혀가면서 다른 섬과 닿으면 그 거리 return
    queue = deque()
    check = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 and visited[i][j] == c:
                queue.append([i, j])
                check[i][j] = 1
    res = bfs(c)
    ans = min(ans, res)


print(ans)