N = int(input())

count = 0  # 그룹 단어가 아닌 단어를 카운트

for i in range(N):
    temp = []
    word = input()
    for j in word:
        if j not in temp:
            temp.append(j)
        else:
            if j == temp[-1]:
                pass
            else:
                count += 1
                break

result = N - count
print(result)