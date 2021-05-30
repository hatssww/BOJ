count = [0] * (ord('z') - ord('a') + 1)

S = input()

for i in S:
    if count[ord(i) - ord('a')] == 0:
        count[ord(i) - ord('a')] = S.count(i)

for j in range(len(count)):
    print(count[j], end=" ")