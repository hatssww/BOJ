S = input()
a = []
for i in range(len(S)):
    a.append(S[i:])
a.sort()
for j in a:
    print(j)