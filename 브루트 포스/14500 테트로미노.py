# dfs방식을 이용한 풀이
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 0]

Tshape = [
    [[0, 1], [0, 2], [-1, 1]],
    [[0, 1], [0, 2], [1, 1]],
    [[1, 0], [2, 0], [1, -1]],
    [[1, 0], [2, 0], [1, 1]]]

n, m = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]

visit = [[0] * m for i in range(n)]
res = 0


def dfs(x, y, cnt, sum):
    global res
    if cnt == 4:
        res = max(res, sum)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            dfs(nx, ny, cnt + 1, sum + A[nx][ny])
            visit[nx][ny] = 0


def Tshape_block(x, y):
    global res
    for i in Tshape:
        try:
            sum = A[x][y] + A[x + i[0][0]][y + i[0][1]] + A[x + i[1][0]][y + i[1][1]] + A[x + i[2][0]][y + i[2][1]]
        except:
            sum = 0
        res = max(res, sum)


for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, 1, A[i][j])
        visit[i][j] = 0
        Tshape_block(i, j)

print(res)