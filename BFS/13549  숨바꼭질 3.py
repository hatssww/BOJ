from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * 100001
visited = [False] * 100001
q = deque()

def bfs(n):
    visited[n] = True
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            return dp[k]
        for nx in (x * 2, x - 1, x + 1):
            if 0 <= nx < 100001 and not visited[nx]:
                if nx == x * 2:
                    visited[nx] = True
                    dp[nx] = dp[x]
                    q.appendleft(nx)
                else:
                    visited[nx] = True
                    dp[nx] = dp[x] + 1
                    q.append(nx)

print(bfs(n))