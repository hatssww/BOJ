# 런타임 에러(재귀함수 시간초과)
# import sys

# n, m = map(int, sys.stdin.readline().split())

# def factorial(n, m):
#     if n == m:
#         return m
#     return n * factorial(n-1, m)

# comb = factorial(n, m) / factorial(m, 1)
# comb = str(int(comb))

# count = 0
# for i in comb[::-1]:
#     if i == '0':
#         count += 1
#     else:
#         break

# print(count)



import sys

n, m = map(int, sys.stdin.readline().split())

def count_number(n, k):
    count = 0
    while n != 0:
        n //= k
        count += n
    return count

five_cnt = count_number(n, 5) - count_number(n - m, 5) - count_number(m, 5)
two_cnt = count_number(n, 2) - count_number(n - m, 2) - count_number(m, 2)

result = min(five_cnt, two_cnt)
print(result)