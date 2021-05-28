def fibonacci(N):
    if N <= 1:
        return N
    return fibonacci(N-2) + fibonacci(N-1)

n = int(input())
print(fibonacci(n))