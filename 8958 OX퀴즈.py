T = int(input())

for i in range(T):
    ox_input = input()
    score = 0
    count = 1
    for j in range(len(ox_input)):
        if ox_input[j] == "O":
            score += count
            count += 1
        else:
            count = 1
    
    print(score)