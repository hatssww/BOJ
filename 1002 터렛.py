import math

T = int(input())

for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    if r1 == r2 and d == 0:  # 같은 원일때
        print(-1)
    elif abs(r1-r2) == d or r1 + r2 == d:  # 내접, 외접 할 때
        print(1)
    elif abs(r1-r2) < d < r1 + r2:  # 두 점에서 만날 때
        print(2)
    else:
        print(0)