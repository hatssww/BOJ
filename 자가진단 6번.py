array = list(map(int, input().split()))

def solution(array):
    keys = set(array)
    keys = list(keys)
    cnt = []
    for i in keys:
        cnt.append(array.count(i))
    res = []
    for i in cnt:
        if i != 1:
            res.append(i)

    if res:
        return res
    else:
        return [-1]

print(solution(array))