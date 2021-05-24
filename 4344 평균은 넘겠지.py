C = int(input())

for i in range(C):
    data = list(map(int, input().split()))
    student_num = data[0]
    scores = data[1:]
    mean = sum(scores) / student_num
    count = 0  # 평균 넘은 학생 수
    for i in scores:
        if i > mean:
            count += 1
    pass_ratio = count / student_num * 100
    print(f"{round(pass_ratio, 3):0.3f}%")