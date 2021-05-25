X = int(input())

col = 1
while col < X:
    X -= col
    col += 1

# a/b
if col % 2 == 0:  # 짝수 열이면 분자 오름차순, 분모 내림차순
    a = X
    b = col - X + 1
else:             # 홀수 열이면 분자 내림차순, 분모 오름차순
    a = col - X + 1
    b = X


print(f"{a}/{b}")