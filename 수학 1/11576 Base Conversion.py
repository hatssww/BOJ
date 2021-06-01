a, b = map(int, input().split())
m = int(input())
A = list(map(int, input().split()))
ten_type = 0
j = m - 1
for i in A:
    ten_type += i * (a**j)
    j -= 1

b_type = []

while ten_type != 0:
    b_type.append(ten_type % b)
    ten_type //= b

for i in range(len(b_type)-1, -1, -1):
    print(b_type[i], end=" ")