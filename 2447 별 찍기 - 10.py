def draw_star(pattern):
    matrix = []
    for i in range(3 * len(pattern)):
        if i // len(pattern) == 1:
            matrix.append(pattern[i % len(pattern)] + " "*len(pattern) + pattern[i % len(pattern)])
        else:
            matrix.append(pattern[i % len(pattern)] * 3)
    return list(matrix)

star = ["***", "* *", "***"]

n = int(input())
cnt = 0

while n != 3:
    n = int(n / 3)
    cnt += 1

for i in range(cnt):
    star = draw_star(star)

for i in star:
    print(i)