import sys
input = sys.stdin.readline
n = int(input())
A = [list(map(str, input().rstrip())) for i in range(n)]
result = 0

def check(array):
    cnt = 0
    for i in range(n):
        count_x = 1
        count_y = 1

        for j in range(n-1):
            if array[i][j] == array[i][j+1]:
                count_x += 1
            else:
                cnt = max(cnt, count_x)
                count_x = 1

            if array[j][i] == array[j+1][i]:
                count_y += 1
            else:
                cnt = max(cnt, count_y)
                count_y = 1
        cnt = max(cnt, count_x, count_y)
    return cnt

for i in range(n):
    for j in range(n-1):
        if A[i][j] != A[i][j+1]:
            tmp = A[i][j]
            A[i][j] = A[i][j+1]
            A[i][j+1] = tmp

            result = max(result, check(A))

            tmp = A[i][j]
            A[i][j] = A[i][j+1]
            A[i][j+1] = tmp
        
        if A[j][i] != A[j+1][i]:
            tmp = A[j][i]
            A[j][i] = A[j+1][i]
            A[j+1][i] = tmp

            result = max(result, check(A))

            tmp = A[j][i]
            A[j][i] = A[j+1][i]
            A[j+1][i] = tmp

print(result)