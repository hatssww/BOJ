# # 쉬운 방법 있는데... 무식하게 풀음
# from collections import deque
# import sys
# input = sys.stdin.readline

# n = int(input())
# tree = [list(map(str, input().rstrip().split())) for _ in range(n)]
# tree.sort()
# ord("A") - 65 == 0

# def preorder():
#     visited = [False] * n
#     res = []
#     q = deque()
#     q.append(tree[0])
#     visited[ord(tree[0][0]) - 65] = True
#     while q:
#         root, l, r = q.popleft()
#         res.append(root)
#         if not visited[ord(root) - 65]:
#             visited[ord(root) - 65] = True
#         if l != '.':
#             q.appendleft(tree[ord(l) - 65])
#         if r != '.':
#             q.append(tree[ord(r) - 65])
#     return res

# def inorder():
#     visited = [False] * n
#     res = []
#     q = deque([tree[0]])
#     while q:
#         root, l, r = q[0]
#         if l != '.' and not visited[ord(l) - 65]:
#             q.appendleft(tree[ord(l) - 65])
#         if l == '.' or visited[ord(l) - 65]:
#             q.popleft()
#             if not visited[ord(root) - 65]:
#                 visited[ord(root) - 65] = True
#                 res.append(root)
#             if r != '.':
#                 q.append(tree[ord(r) - 65])
#     return res

# # 미해결(얘만)
# def postorder():
#     visited = [False] * n
#     res = []
#     q = deque([tree[0]])
#     while q:
#         root, l, r = q[0]
#         if r != '.' and not visited[ord(r) - 65]:
#             q.appendleft(tree[ord(r) - 65])
#         if l != '.' and not visited[ord(l) - 65]:
#             q.appendleft(tree[ord(l) - 65])
#             continue
        
#         if l == '.' or visited[ord(l) - 65]:
#             q.popleft()
#             if not visited[ord(root) - 65]:
#                 visited[ord(root) - 65] = True
#                 res.append(root)
#             if r == '.' or not visited[ord(r) - 65]:
#                 q.popleft()
#                 visited[ord(r) - 65] = True
#                 res.append(r)

#         print(root, l, r, q)
#     return res

# print(preorder())
# print(inorder())
# print(postorder())


# 쉬운 풀이
import sys
input = sys.stdin.readline

n = int(input())
tree = {}

for _ in range(n):
    root, left, right = map(str, input().strip().split())
    tree[root] = [left, right]


def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])


def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])


def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')