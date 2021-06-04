# DFS 완전탐색(시간 초과)
import sys
input = sys.stdin.readline

n = int(input())
N = [list(map(int, input().split())) for i in range(n)]
stack = []
visited = [[False] * (n + 1) for i in range(n + 1)]
result = 4000001

def dfs(depth, k):
    global result
    if depth == n:
        result = min(result, sum(stack))
        return

    for i in range(1, n + 1):
        if not visited[k][i] and i != k:
            visited[k][i], visited[i][k] = True, True
            stack.append(N[k-1][i-1])
            dfs(depth + 1, i)
            visited[k][i], visited[i][k] = False, False
            stack.pop()

dfs(0, 1)
print(result)


# 비트마스크를 이용한 메모이제이션(Top-down, Memoization) 방식 이용
import sys
input = sys.stdin.readline
n = int(input())
P = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (1<<n) for _ in range(n)]


def cost(now, before):
    if dp[now][before]:
        return dp[now][before]
    
    if before == (1<<n) - 1:
        return P[now][0] if P[now][0] > 0 else sys.maxsize

    res = sys.maxsize
    for i in range(1, n):
        if not (before>>i) % 2 and P[now][i]:
            tmp = cost(i, before|(1<<i))  # before + (1<<i), 이전에 방문한것 + 다음 방문할 것 기록
            res = min(res, P[now][i] + tmp)
    
    dp[now][before] = res
    return res


print(cost(0, 1))