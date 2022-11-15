n = int(input())
Q1 = Q2 = Q3 = Q4 = AXIS = 0
for i in range(n):
    a, b = map(int, input().split())
    if a > 0 and b > 0:
        Q1 += 1
    elif a > 0 and b < 0:
        Q4 += 1
    elif a < 0 and b > 0:
        Q2 += 1
    elif a < 0 and b < 0:
        Q3 += 1
    else:
        AXIS += 1
print('Q1: {}'.format(Q1))
print('Q2: {}'.format(Q2))
print('Q3: {}'.format(Q3))
print('Q4: {}'.format(Q4))
print('AXIS: {}'.format(AXIS))
