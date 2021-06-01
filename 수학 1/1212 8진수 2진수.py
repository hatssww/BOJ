import sys

n = sys.stdin.readline().rstrip()

bin = format(int('0o' + n, 8), 'b')
print(bin)