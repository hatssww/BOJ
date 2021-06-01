import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
d = A.copy()
for i in range(n):
    temp = []
    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            temp.append(d[j])
    if temp:
        d[i] = A[i] + max(temp)

print(max(d))