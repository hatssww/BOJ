import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(ch, cnt, x, y, sx, sy):
    global is_true
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if is_true:
            return
        if 0 <= nx <= n - 1 and 0 <= ny <= m - 1 and arr[nx][ny] == ch:
            if cnt >=4 and nx == sx and ny == sy:
                is_true = True
                return True
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(ch, cnt + 1, nx, ny, sx, sy)
                visited[nx][ny] = 0
    return False


n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append([])
    s = input().rstrip()
    for j in s:
        arr[i].append([j])

visited = [[0] * m for _ in range(n)]
is_true = False

for i in range(n):
    for j in range(m):
        ch = arr[i][j]
        visited[i][j] = 1
        dfs(ch, 1, i, j, i, j)
        if is_true:
            break
    if is_true:
            break

print("Yes" if is_true else "No")