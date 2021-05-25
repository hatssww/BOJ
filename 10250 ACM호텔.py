T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())

    floor = N % H
    if floor == 0:
        floor = H
        room = N // H
    else:
        room = N // H + 1 

    if room < 10:
        print(f"{floor}0{room}")
    else:
        print(f"{floor}{room}")