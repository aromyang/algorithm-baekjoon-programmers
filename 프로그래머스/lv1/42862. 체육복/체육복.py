def solution(n, lost, reverse):
    answer = 0
    stu = [1 for _ in range(n + 1)]
    for i in range(1, n + 1):
        if i in lost:
            stu[i] -= 1
        if i in reverse:
            stu[i] += 1

    for i, s in enumerate(stu):
        if i == 1:
            if stu[i] == 2 and stu[i + 1] == 0:
                stu[i + 1] += 1
                stu[i] -= 1
            continue
        elif s == 2:
            if stu[i - 1] == 0:
                stu[i - 1] += 1
                stu[i] -= 1
                continue
            elif i != n and stu[i + 1] == 0:
                stu[i + 1] += 1
                stu[i] -= 1

    return stu[1:].count(1) + stu[1:].count(2)

