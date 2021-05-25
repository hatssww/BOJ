T = int(input())

for t in range(T):
    x, y = map(int, input().split())

    max_k = 1
    max_distance = 0
    count = 0
    distance = y - x
    while max_distance < distance:
        count += 1

        
        max_distance += max_k
        if count % 2 == 0:
            max_k += 1

    print(count)