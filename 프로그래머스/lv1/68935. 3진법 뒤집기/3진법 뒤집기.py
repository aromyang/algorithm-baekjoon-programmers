def to_three(num):
    three = ''
    while num > 0:
        num, mod = divmod(num, 3)
        three += str(mod)
    return three


def solution(n):
    return int(to_three(n), 3)


print(solution(125))
