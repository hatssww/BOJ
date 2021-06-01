import sys
input = sys.stdin.readline
T = int(input())

for t in range(T):
    n = int(input())
    d = [[0, 0] for _ in range(n + 1)]
    A = [[0] + list(map(int, input().split())) for _ in range(2)]

    d[1][0] = A[0][1]
    d[1][1] = A[1][1]

    for i in range(2, n+1):
                d[i][0] = max(d[i-1][1] + A[0][i], d[i-2][1] + A[0][i])
                d[i][1] = max(d[i-1][0] + A[1][i], d[i-2][0] + A[1][i])

    print(max(d[n]))