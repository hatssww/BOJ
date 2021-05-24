first = int(input())
second = input()

result = 0
for i in range(len(second)):
    temp = first * int(second[-1-i])
    print(temp)
    result += (temp * 10**i)

print(result)