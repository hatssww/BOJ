N = int(input())

if N < 100:
    print(N)  # 1 ~ 99까지는 모두 한수
else:
    count = 99
    for i in range(100, N+1):
        i = str(i)
        if (int(i[-1]) - int(i[-2])) == (int(i[-2]) - int(i[0])):
            count += 1

    print(count)