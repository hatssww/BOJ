while True:
    try:
        result = [0, 0, 0, 0]
        S = input()

        for i in S:
            if i.isspace():
                result[3] += 1
            elif i.isalpha():
                if i.isupper():
                    result[1] += 1
                else:
                    result[0] += 1
            else:
                result[2] += 1

        for j in range(4):
            print(result[j], end=" ")
        print()
    except EOFError:
        break