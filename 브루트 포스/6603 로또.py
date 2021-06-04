import sys
input = sys.stdin.readline


def dfs(s, j, depth):
    if depth == 6:
        
        res.add(tuple(stack))
        return

    for i in range(j, len(s)):
        if not visited[i]:
            visited[i] = True
            stack.append(s[i])
            dfs(s, i + 1, depth + 1)
            visited[i] = False
            stack.pop()


while True:
    numbers = list(map(int, input().split()))
    k = numbers[0]
    if k == 0:
        break
    s = numbers[1:]
    visited = [False] * 13
    stack = []
    res = set()
    dfs(s, 0, 0)
    res = list(res)
    res.sort()    
    for i in res:
        print(" ".join(map(str, i)))
    print()