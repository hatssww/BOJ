rests = set([])

for i in range(10):
    in_num = int(input())
    rest = in_num % 42
    rests.add(rest)

print(len(rests))