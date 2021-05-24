import sys

N = int(sys.stdin.readline().rstrip())
num = N
count = 0
while True:
    sum_num = (num // 10) + (num % 10)
    new_num = ((num % 10) * 10) + (sum_num % 10)
    count += 1
    if new_num == N:
        break
    num = new_num
print(count)


# 풀리긴 하지만 시간초과

# import sys

# N = sys.stdin.readline().rstrip()
# num = N
# count = 0
# while True:
#     if int(num) < 10:
#         num = "0" + num
#     sum = int(num[0])+int(num[1])
#     new_num = num[-1] + str(sum)[-1]
#     count += 1
#     if new_num != N:
#         num = new_num
#     else:
#         break
# print(count)