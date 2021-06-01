import math
import sys

n, s = map(int, sys.stdin.readline().split())
A_list = list(map(int, sys.stdin.readline().split()))
distance = []
for i in range(n):
    distance.append(abs(A_list[i] - s))

d = min(distance)
for i in range(len(distance)):
    d = math.gcd(d, distance[i])

print(d)