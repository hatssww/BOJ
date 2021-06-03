import sys
input = sys.stdin.readline

n = int(input())
N = len(str(n))
result = 0
if N == 1:
    print(n)
else:
    for i in range(N-1, -1, -1):
        if i == N - 1:
            last = ((n - 10**i) + 1) * (i + 1)
            result += last
        else:
            result += 9 * (10**i) * (i + 1)

    print(result)