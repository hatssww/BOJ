def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    
    for i in range(2, int(num**0.5)+1):  # 제곱근까지만 검사
        if num % i == 0:
            return False
    return True

M, N = map(int, input().split())

for num in range (M, N+1):
    if is_prime(num):
        print(num)