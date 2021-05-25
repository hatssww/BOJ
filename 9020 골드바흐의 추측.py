def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


T = int(input())
for t in range(T):
    n = int(input())
    primes = set()
    for i in range(2, n+1):
        if is_prime(i):
            primes.add(i)
    
    a = n // 2
    for x in range(a, 1, -1):
        if (n-x in primes) and (x in primes):
            print(x, n-x)
            break