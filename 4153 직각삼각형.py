while True:
    a, b, c = map(int, input().split())
    sides = [a, b, c]
    sides.sort()

    if a == 0 and b == 0 and c == 0:
        break

    if sides[2]**2 == (sides[0]**2 + sides[1]**2):
        print("right")
    else:
        print("wrong")