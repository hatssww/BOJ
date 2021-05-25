T = int(input())

for x in range(T):

    k = int(input())
    n = int(input())

    apartment = [[]]
    for i in range(n):
        apartment[0].append(i+1)

    for i in range(1, k+1):
        floor = []
        sum = 0
        for j in range(n):
            sum += apartment[i-1][j]
            floor.append(sum)
        apartment.append(floor)

    print(apartment[k][n-1])