import sys
from itertools import combinations

def gcd(n, m):
    n = max(n, m)
    m = min(n, m)
    if n % m != 0:
        return gcd(m, n % m)
    else:
        return m


t = int(sys.stdin.readline())

for _ in range(t):
    N = list(map(int, sys.stdin.readline().split()))

    data = N[1:]
    data.sort(reverse=True)
    comb = list(combinations(data, 2))
    result = []
    for i in range(len(comb)):
        result.append(gcd(comb[i][0], comb[i][1]))
    print(sum(result))