t = int(input())
for i in range(t):
    math = input().split()
    result = float(math[0])
    for j in math:
        if j == '@':
            result *= 3
        if j == '%':
            result += 5
        if j == '#':
            result -= 7
    print('%.2f' % result)
