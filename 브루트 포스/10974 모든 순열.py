import sys
input = sys.stdin.readline

n = int(input())
stack = []
visited = [False] * (n + 1)

def dfs(depth):
    if depth == n:
        print(' '.join(map(str, stack)))
        return
    over = 0
    for i in range(1, n + 1):
        if not visited[i] and over != i:
            visited[i] = True
            over = i
            stack.append(i)
            dfs(depth + 1)
            visited[i] = False
            stack.pop()

dfs(0)