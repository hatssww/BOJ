import sys


def gcd(n, m):
    if n % m == 0:
        return m
    else:
        return gcd(m, n % m)


def lcm(n, m):
    return (n * m) // gcd(n, m)


T = int(sys.stdin.readline())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a, b))