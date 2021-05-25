import sys

A, B = map(str, sys.stdin.readline().split())
A_reverse = []
B_reverse = []

for i in range(3):
    A_reverse.append(A[-1 - i])
    B_reverse.append(B[-1 - i])
    
sangsu_A = A_reverse[0] + A_reverse[1] + A_reverse[2]
sangsu_B = B_reverse[0] + B_reverse[1] + B_reverse[2]

result = [int(sangsu_A), int(sangsu_B)]
print(max(result))