import sys
input = sys.stdin.readline

max = 100000
control = 1000000009

d = [[0, 0, 0, 0] for _ in range(max + 1)]
d[1] = [0, 1, 0, 0]  # 각 숫자를 만드는 조합 중에서 마지막에 오는 숫자가 [1], [2], [3]인 경우를 각각 카운트해서 기록
d[2] = [0, 0, 1, 0]
d[3] = [0, 1, 1, 1]

for i in range(4, max + 1):
    d[i][1] = (d[i-1][2] + d[i-1][3]) % control  # i를 만드는 조합 중에 끝에 오는 숫자가 1이면 그 전단계에는 1이 오지 못하므로, i-1을 만드는 조합 중에서 2로 끝났을 조합의 카운트와 3으로 끝났을 조합의 카운트를 더해서 구함
    d[i][2] = (d[i-2][1] + d[i-2][3]) % control
    d[i][3] = (d[i-3][1] + d[i-3][2]) % control

t = int(input())
for _ in range(t):
    n = int(input())
    print(sum(d[n]) % control)