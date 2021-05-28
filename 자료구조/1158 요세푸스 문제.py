import sys

n, k = map(int, sys.stdin.readline().split())

saving = []
for i in range(n):
    saving.append(i + 1)

result = []
kill = 0
while len(saving) > 0:
    kill = (kill + (k - 1)) % len(saving)
    result.append(str(saving.pop(kill)))

print('<', ", ".join(result)[:], ">", sep='')