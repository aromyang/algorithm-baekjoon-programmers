t = int(input())


def ps(p):
    an = 0
    for pp in p:
        if pp == '(':
            an += 1
        else:
            if an == 0:
                return -1
            else:
                an -= 1
    return an


for _ in range(t):
    if ps(input()):
        print('NO')
    else:
        print('YES')
