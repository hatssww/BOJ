import itertools
import sys

n, m = map(int, sys.stdin.readline().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().rstrip())))

def to_matrix(x, m):
    return [x[i:i + m] for i in range(0, len(x), m)]

a = itertools.product([0, 1], repeat=n * m)
ans = 0

for x in a:
    bit_mask = to_matrix(x, m)
    
    # 가로 방향 조각 더하기(0이면 더하고 1이면 중단)
    sum_h = 0
    for i in range(n):
        hori = 0
        for j in range(m):
            if bit_mask[i][j] == 0:
                hori = 10 * hori + paper[i][j]
            if bit_mask[i][j] == 1 or j == m - 1:
                sum_h += hori
                hori = 0

    # 세로 방향 조각 더하기(1이면 더하고 0이면 중단)
    sum_v = 0
    for j in range(m):
        vert = 0
        for i in range(n):
            if bit_mask[i][j] == 1:
                vert = 10 * vert + paper[i][j]
            if bit_mask[i][j] == 0 or i == n - 1:
                sum_v += vert
                vert = 0

    sum_all = sum_h + sum_v
    ans = max(ans, sum_all)

print(ans)