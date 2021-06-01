ch = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, m = map(int, input().split())
result = ""

while n != 0:
    result = str(ch[n % m]) + result
    n //= m

print(result)