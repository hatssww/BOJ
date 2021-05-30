# print(ord('a'), ord('A'), ord('z'), ord('Z'))

import sys

line = list(sys.stdin.readline().rstrip())

for i in range(len(line)):
    # 대문자 65~90
    if line[i].isupper():
        if ord(line[i]) < (65 + 13):
            line[i] = chr(ord(line[i]) + 13)
        else:
            line[i] = chr(ord(line[i]) - 13)
    # 소문자 97~122
    elif line[i].islower():
        if ord(line[i]) < (97 + 13):
            line[i] = chr(ord(line[i]) + 13)
        else:
            line[i] = chr(ord(line[i]) - 13)

for j in line:
    print(j, end="")