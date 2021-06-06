import sys
input = sys.stdin.readline
n = int(input())
S = set()
for _ in range(n):
    order = input().strip().split()

    if len(order) == 1:
        if order[0] == 'all':
            S = set(i for i in range(1, 21))
        else:
            S = set()
        continue

    command, x = order[0], int(order[1])
    
    if command == 'add':
        S.add(x)
    elif command == 'remove':
        S.discard(x)
    elif command == 'check':
        print(1 if x in S else 0)
    elif command == 'toggle':
        if x in S:
            S.discard(x)
        else:
            S.add(x)