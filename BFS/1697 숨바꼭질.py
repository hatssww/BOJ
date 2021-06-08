from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * 100001
q = deque()

def bfs(n):
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            return dp[k]
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < 100001 and not dp[nx]:
                dp[nx] = dp[x] + 1
                q.append(nx)

print(bfs(n))