import sys
input = sys.stdin.readline

L, C = map(int, input().split())
char = list(map(str, input().split()))
char.sort()
vowel = {'a', 'e', 'i', 'o', 'u'}
cons = set(char) | vowel
res = set()
stack = []
visited = [False] * 16


def dfs(s, j, depth):
    if depth == L:
        v_check = 0
        c_check = 0
        for i in range(L):
            if stack[i] in vowel: v_check += 1
            else: c_check += 1
        if v_check >= 1 and c_check >= 2:
            res.add(tuple(stack))
        return

    for i in range(j, len(s)):
        if not visited[i]:
            visited[i] = True
            stack.append(s[i])
            dfs(s, i + 1, depth + 1)
            visited[i] = False
            ch = stack.pop()


dfs(char, 0, 0)
res = list(res)
res.sort()

for i in res:
    print(''.join(map(str, i)))