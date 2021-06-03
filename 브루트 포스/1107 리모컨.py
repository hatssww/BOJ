import sys
input = sys.stdin.readline
n = int(input())
b = int(input())
normals = {str(i) for i in range(10)}
if b != 0:
        normals -= set(map(str, input().split()))
now = 100
cnt = abs(now - n)

for i in range(1000001):  # +누르는 경우와 - 누르는 경우를 합해 100만
    for j in range(len(str(i))):
        if (str(i))[j] not in normals:
            break
        elif len(str(i)) - 1 == j:
            cnt = min(cnt, abs(n - i) + len(str(i)))

print(cnt)