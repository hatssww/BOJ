from collections import Counter

A = int(input())
B = int(input())
C = int(input())

multi = A * B * C

counters = dict(Counter(str(multi)))

for i in range(10):
    if str(i) in counters:
        print(counters.get(str(i)))
    else:
        print(0)