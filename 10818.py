import sys
N = sys.stdin.readline().rstrip()
numbers = list(map(int, input().split()))

print(f"{min(numbers)} {max(numbers)}")