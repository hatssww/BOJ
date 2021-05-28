# # 시간초과
# import sys
# input = sys.stdin.readline

# # 문자열 입력 받기
# N = sys.stdin.readline().rstrip()
# n = len(N)
# # 커서 위치
# i = n

# # 명령어 입력 받기
# m = int(input())
# for _ in range(m):
#     M = sys.stdin.readline().rstrip()
#     # 명령어
#     if M[0] == 'D':
#         if i != n:
#             i += 1
#         else: continue
#     elif M[0] == 'L':
#         if i != 0:
#             i -= 1
#         else: continue
#     elif M[0] == 'B':
#         if i != 0:
#             N = N[0:i-1] + N[i:]
#             i -= 1
#         else: continue
#     elif M[0] == 'P':
#         N = N[0:i] + M[2] + N[i:]
#         i += 1

# print(N)


# 스택을 이용한 풀이
import sys

st1 = list(sys.stdin.readline().strip())
st2 = []
m = int(sys.stdin.readline())
n = len(st1)

for i in range(m):
    M = sys.stdin.readline()
    if M[0] == 'D' and st2:
        st1.append(st2.pop())
    elif M[0] == 'L' and st1:
        st2.append(st1.pop())
    elif M[0] == 'B'and st1:
        st1.pop()
    elif M[0] == 'P':
        st1.append(M[2])

print("".join(st1 + st2[::-1]))