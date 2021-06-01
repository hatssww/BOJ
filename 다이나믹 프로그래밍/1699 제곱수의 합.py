# # 답은 맞았는데 다이나믹 프로그래밍이 아니라 틀렸다고 채점됨
# import math
# import sys

# n = int(sys.stdin.readline())

# count = 0
# while n != 0:
#     a = int(math.sqrt(n))
#     n -= a**2
#     count += 1

# print(count)


import sys

n = int(sys.stdin.readline())
d = [0] * 100001

for i in range(1, n + 1):
    d[i] = i
    for j in range(1, i):
        if (j * j) > i:
            break
        d[i] = min(d[i - j * j] + 1, d[i])

print(d[n])