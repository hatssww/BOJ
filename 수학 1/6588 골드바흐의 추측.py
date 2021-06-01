import sys


def eratos(n):
    check = [False, False] + [True] * (n - 1)
    for i in range(2, int(n**0.5) + 1):
        if check[i] == True:
            for j in range(i + i, n + 1, i):
                check[j] = False
    return check


check = eratos(1000000)

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    j = n
    for i in range(n):
        if check[i] and check[j]:
            print(f"{n} = {i} + {j}")
            break
        j -= 1
    else:
        print("Goldbach's conjecture is wrong.")