word = input()

num2 = ['A', 'B', 'C']
num3 = ['D', 'E', 'F']
num4 = ['G', 'H', 'I']
num5 = ['J', 'K', 'L']
num6 = ['M', 'N', 'O']
num7 = ['P', 'Q', 'R', 'S']
num8 = ['T', 'U', 'V']
num9 = ['W', 'X', 'Y', 'Z']

time = 0
for i in word:
    if i in num2:
        time += 3
    elif i in num3:
        time += 4
    elif i in num4:
        time += 5
    elif i in num5:
        time += 6
    elif i in num6:
        time += 7
    elif i in num7:
        time += 8
    elif i in num8:
        time += 9
    elif i in num9:
        time += 10

print(time)