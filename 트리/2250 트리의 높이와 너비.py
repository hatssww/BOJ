import sys
input = sys.stdin.readline

n = int(input())
tree = {}
parent = [0] * (n + 1)
for _ in range(n):
    root, left, right = map(int, input().strip().split())
    tree[root] = [left, right]
    parent[root] += 1
    if left != -1:
        parent[left] += 1
    if right != -1:
        parent[right] += 1

for i in range(1, n + 1):
    if parent[i] == 1:
        start_root = i

dp = [[] for _ in range(n + 1)]
cnt = 1


def inorder(root, level):
    global cnt
    if root != -1:
        inorder(tree[root][0], level + 1)
        dp[level].append(cnt)
        cnt += 1
        inorder(tree[root][1], level + 1)


inorder(start_root, 1)
res = max(dp[1]) - min(dp[1]) + 1
level = 1
for i in range(2, n + 1):
    if dp[i]:
        if res < max(dp[i]) - min(dp[i]) + 1:
            res = max(dp[i]) - min(dp[i]) + 1
            level = i

print(level, res)