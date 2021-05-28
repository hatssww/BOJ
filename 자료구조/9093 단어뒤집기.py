import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    sentence = list(map(str, input().split()))
    for i in sentence:
        for j in range(len(i)):
            print(i[-1 - j], end="")
        print(end=" ")
    print()