def kaprekar(n):
    for i in str(n):
        n += int(i)

    return n

n = 1
kaprekar_set = set([])
while n <= 10000:
    kaprekar_set.add(kaprekar(n))
    n += 1

int_set = set(range(1, 10001))
selfnumber = list(int_set - kaprekar_set)
selfnumber.sort()

for i in range(len(selfnumber)):
    print(selfnumber[i])