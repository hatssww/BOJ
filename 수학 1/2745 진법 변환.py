ch = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, b = map(str, input().split())
b = int(b)
result = 0
j = len(n) - 1
for i in n:
    a = ch.index(i)
    result += a * (b**j)
    j -= 1

print(result)