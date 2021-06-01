import sys
n = sys.stdin.readline().rstrip()
octal = oct(int(n, 2))
octal = octal[2:]
print(int(octal))