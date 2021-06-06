import sys
input = sys.stdin.readline

n = int(input())
map = []
for _ in range(n):
    map.append(input().rstrip())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * n for _ in range(n)]
check = 0
res = []

def dfs (x, y):
    global check
    if map[x][y] == '0':
        return
    
    visited[x][y] = True
    check += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx <= n - 1) and (0 <= ny <= n - 1):
            if not visited[nx][ny]:
                dfs(nx, ny)
    

for i in range(n):
    for j in range(n):
        if map[i][j] == '0':
            continue
        if not visited[i][j]:
            dfs(i, j)
            res.append(check)
            check = 0

print(len(res))
for i in sorted(res):
    print(i)