import sys
input = sys.stdin.readline

n = int(input())
N = list(map(int, input().split()))

def prev_permutation(n, a):
    i = n - 1
    while i > 0 and a[i-1] <= a[i]:  # 작은 숫자가 앞으로 가야 함
        i -= 1
    if i <= 0:
        return False

    j = n - 1
    while a[i-1] <= a[j]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]

    j = n - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True


if prev_permutation(n, N):
    print(' '.join(map(str, N)))
else:
    print(-1)