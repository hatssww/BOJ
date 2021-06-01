import sys

def eratos(n):
    check = [False, False] + [True] * (n - 1)
    for i in range(2, int(n**0.5) + 1):
        if check[i] == True:
            for j in range(i + i, n + 1, i):
                check[j] = False
    return check

t = int(sys.stdin.readline())
N = [int(sys.stdin.readline()) for _ in range(t)]
check = eratos(max(N))

for n in N:
    count = 0
    for i in range(n // 2 + 1):

        
        if check[i] and check[n - i]:
            count += 1

    print(count)