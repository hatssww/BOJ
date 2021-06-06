import sys
input = sys.stdin.readline
n, s = map(int, input().split())
S = list(map(int, input().split()))
count = 0

def solve(idx, sum):
    global count
    if idx == n:
        return
    sum += S[idx]
    if sum == s:
        count += 1
    solve(idx + 1, sum - S[idx])
    solve(idx + 1, sum)

solve(0, 0)
print(count)