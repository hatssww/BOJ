# 답은 나오는데 OverflowError 뜸
# import sys
# from collections import Counter

# d = [[1, 1],
#     [0, 2],
#     [1, 3],
#     [2, 4],
#     [3, 5],
#     [4, 6],
#     [5, 7],
#     [6, 8],
#     [7, 9],
#     [8, 8]]


# n = int(sys.stdin.readline())

# check = [True] * 10 + [False] * (10**n - 10)
# check[0] = False

# for i in range(10, 10**n):
#     s = str(i)
#     istrue = True
#     for j in range(len(s) - 1):
#         if int(s[j]) in d[int(s[j+1])]:
#             continue
#         else:
#             istrue = False
#             break
#     if istrue:
#         check[i] = True

# result = Counter(check[10**(n-1):])
# print(result[True] % 1000000000)


import sys
n = int(sys.stdin.readline())

d = [[0 for i in range(10)] for j in range(101)]

for i in range(1, 10):
    d[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            d[i][j] = d[i - 1][1]
        elif j == 9:
            d[i][j] = d[i - 1][8]
        else:
            d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1]

print(sum(d[n]) % 1000000000)