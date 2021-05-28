X = []
Y = []

for i in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for j in X:
    if X.count(j) == 1:
        x = j

for k in Y:
    if Y.count(k) == 1:
        y = k

print(x, y)