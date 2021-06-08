from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * 100001
move = [0] * 100001
q = deque()

def bfs(n):
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dp[k])
            path(k)
            return x
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < 100001 and not dp[nx]:
                dp[nx] = dp[x] + 1
                move[nx] = x  # 이전 경로들 저장
                q.append(nx)

def path(k):  # 정답부터 거꾸로 경로 추적
    res = []
    tmp = k
    for i in range(dp[k] + 1):
        res.append(tmp)
        tmp = move[tmp]
    print(' '.join(map(str, res[::-1])))


bfs(n)