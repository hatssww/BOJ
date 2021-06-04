# # 안풀림 ㅠ
# import sys
# input = sys.stdin.readline

# n = int(input())
# s = input().rstrip()
# S = []
# for i in range(n):
#     tmp = 'o'*i + s[:n-i]
#     S.append(tmp)
#     s = s[n-i:]

# result = []

# def is_True(num, i, x, y):
#     if sum(num[x:]) + i > 0 and S[x][y] == '+':
#         return True
#     if sum(num[x:]) + i < 0 and S[x][y] == '-':
#         return True
#     if sum(num[x:]) + i == 0 and S[x][y] == '0':
#         return True
#     else:
#         return False

# off = False
# def solve(depth, num, x, y):
#     global off
#     if off:
#         return
#     if depth == n:
#         print(' '.join(map(str, num)))
#         off = True
#         return

#     for i in range(-10, 11):
#         if depth == 0:
#             solve(depth + 1, num + [i], x, y)
#         if is_True(num, i, x, y):
#             if y != n - 1:
#                 solve(depth + 1, num + [i], x, y + 1)
#             else:
#                 solve(depth + 1, num + [i], x + 1, x + 1)

# solve(0, [], 0, 0)


# ans에 숫자 기록해가면서 탐색
import sys
input = sys.stdin.readline

def check(index):  # sign[i][index]의 부호 조건을 만족하는지 아닌지 검사하는 함수(역순)
    s = 0
    for i in range(index, -1, -1):
        s += ans[i]
        if sign[i][index] == 0:
            if s != 0:
                return False
        elif sign[i][index] < 0:
            if s >= 0:
                return False
        elif sign[i][index] > 0:
            if s <= 0:
                return False
    return True

def solve(index):  # 현재 index 번째 수를 채우는 함수
    if index == n:
        return True
    if sign[index][index] == 0:
        ans[index] = 0
        return check(index) and solve(index + 1)
    
    for i in range(1, 11):
        ans[index] = i * sign[index][index]    # 각 숫자에 부호를 입혀줌
        if check(index) and solve(index + 1):
            return True
    return False

n = int(input())
ans = [0] * n
signs = list(input())
sign = [[0] * n for _ in range(n)]

idx = 0
for i in range(n):
    for j in range(i, n):
        if signs[idx] == "+":
            sign[i][j] = 1
        elif signs[idx] == "-":
            sign[i][j] = -1
        idx += 1

solve(0)
print(" ".join(map(str, ans)))