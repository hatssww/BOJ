import sys
input = sys.stdin.readline

k = int(input())
s = list(map(str, input().split()))
visited = [False] * 10
mx, mn = "", ""

def symbol(i, j, c):
    if c == '<':
        return i < j
    if c == '>':
        return i > j

def solve(depth, string):
    global mx, mn
    if depth == k + 1:
        if not len(mn):
            mn = string
        else:
            mx = string
        return
    for i in range(10):
        if not visited[i]:
            if depth == 0 or symbol(string[-1], str(i), s[depth - 1]):
                visited[i] = True
                solve(depth + 1, string + str(i))
                visited[i] = False

solve(0, "")
print(mx)
print(mn)