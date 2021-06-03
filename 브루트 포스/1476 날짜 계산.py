import sys
input = sys.stdin.readline
e, s, m = map(int, input().split())
E, S, M, n = 1, 1, 1, 1

while True:
    if E == e and S == s and M == m:
        break
    E += 1; S += 1; M += 1; n += 1
    if E >= 16: E -= 15
    if S >= 29: S -= 28
    if M >= 20: M -= 19

print(n)