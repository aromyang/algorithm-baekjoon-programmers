n = int(input())
for i in range(2 * n - 1, 0, -2):
    s = ((2 * n) - i) // 2
    print(' ' * s + '*' * i)
