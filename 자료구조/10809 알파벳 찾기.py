index = [-1] * (ord('z') - ord('a') + 1)

S = input()

for i in S:
    if index[ord(i) - ord('a')] == -1:
        index[ord(i) - ord('a')] = S.index(i)

for j in range(len(index)):
    print(index[j], end=" ")