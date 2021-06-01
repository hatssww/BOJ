# import sys
# import math
# n, m = map(int, sys.stdin.readline().split())

# print(math.gcd(n, m))
# print(math.lcm(n, m))

import sys

def gcd(n, m):
    if n % m != 0:
        return gcd(m, n % m)
    else:
        return m


def lcm(n, m):
    return n * m // gcd(n, m)


n, m = map(int, sys.stdin.readline().split())

print(gcd(n, m))
print(lcm(n, m))