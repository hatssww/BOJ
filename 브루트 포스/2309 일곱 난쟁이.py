import sys
input = sys.stdin.readline
A = [int(input()) for i in range(9)]

for i in range(1, 9):
    for j in range(i):
        if sum(A[ : j] + A[j + 1 : i] + A[i + 1 : ]) == 100:
            A = A[ : j] + A[j + 1 : i] + A[i + 1 : ]
A.sort()
for i in A:
    print(i)