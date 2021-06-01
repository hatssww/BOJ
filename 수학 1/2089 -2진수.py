import sys

n = int(sys.stdin.readline())
result = ""
if n == 0:
    print(0)
else:
    while n != 0:
        if n % (-2) == 0:
            result = '0' + result
            n = n // (-2)
        else:
            result = '1' + result
            n = n // (-2) + 1

print(result)

# -로 나누는 것은 몫도 -로 뜨는데, 이때 몫은 -값의 절댓값이므로
# 만약 6//(-4) = -1.xxx 이기 때문에 몫은 -2가 됨