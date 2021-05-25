T = int(input())

for i in range(T):
    R, S = map(str, input().split())
    R = int(R)
    for j in S:
        print(j * R, end="")
    print()