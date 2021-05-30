import sys

S = sys.stdin.readline().rstrip()
temp = []
while len(S) > 0:
    if S[0] == "<":
        index = S.find(">")
        print(S[0 : index + 1], end="")
        S = S[index + 1:]
    elif S[0] == " ":
        print(S[0], end="")
        S = S[1:]
    else:
        while len(S) > 0:
            if S[0] != " " and S[0] != "<":
                temp.append(S[0])
                S = S[1:]
            else:
                break
        print("".join(temp[::-1]), end="")
        temp = []