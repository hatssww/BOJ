import sys
input = sys.stdin.readline

T = int(input())

def year(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return  x
        x += m
    return -1

for i in range(T):
    M, N, x, y = map(int, input().split())
    result = year(M, N, x, y)
    print(result)


# # 메모리 초과
# d = [[0] * 40001 for i in range(40001)]

# x, y, n = 1, 1, 1
# for i in range(1, 40001):
#     for j in range(1, 40001):
#         x += 1; y += 1; n += 1
#         if x >= i + 1: x -= i
#         if y >= j + 1: y -= j
        
#         d[i][j] = [n, x, y]

# for i in range(T):
#     M, N, X, Y = map(int, input().split())
#     A = d[M][N]
#     if A[1] == X and A[2] == Y:
#         print(A[0])
#     else:
#         print(-1)


# # 첫 시도 시간 초과
# for i in range(T):
#     M, N, X, Y = map(int, input().split())
#     x, y, n = 1, 1, 1
#     is_false = False
#     while True:
#         if X == x and Y == y:
#             break
#         x += 1; y += 1; n += 1
#         if x >= M + 1: x -= M
#         if y >= N + 1: y -= N
#         if x == 1 and y == 1:
#             is_false = True
#             break
#     if is_false:
#         print(-1)
#     else:
#         print(n)