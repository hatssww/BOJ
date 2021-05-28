def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else: 
        hanoi(n-1, a, c, b)  # n-1개의 하노이 탑을 2번째 위치에 가져다 둠(다 옮겨졌다고 가정)
        print(a, c)          # n번째 원판을 1 → 3번으로 이동
        hanoi(n-1, b, a, c)  # 2번에 있던 n-1개의 하노이 탑을 다시 1번 위치로 옮겼다고 생각하고 반복


num = int(input())
sum = 1
for i in range(num-1):
    sum = sum * 2 + 1

print(sum)
hanoi(num, 1, 2, 3)